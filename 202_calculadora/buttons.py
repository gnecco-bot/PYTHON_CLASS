import math
# from display import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;') # Maneira que pode ser sobrescrevida
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True) # Italico
        # font.setBold(True) # Negrito
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setCheckable(True) # Deixa checado a tecla selecionada


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    
    def _makeGrid(self): # Operador
        self.display.eqPressed.connect(self._eq) # Conecta o sinal eqRequested do display ao método _eq
        self.display.delpressed.connect(self._backspace) # Conecta o sinal delpressed do display ao método backspace
        self.display.clearPressed.connect(self._clear) # Conecta o sinal clearPressed do display    
        self.display.imputPressed.connect(self._insertToDisplay) # Conecta o sinal imputPressed do display ao método _insertButtonTextToDisplay
        self.display.operatorpressed.connect(self._configLeftOp) # Conecta o sinal operatorpressed do display ao método _operatorClicked

        for row_number, row in enumerate(self._gridMask):
            for column_number, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            # slot = self._makeSlot(self.display.clear) # Método 1
            # self._connectButtonClicked(button, slot) # Método 1
            # button.clicked.connect(self.display.clear) # Método 2
            self._connectButtonClicked(button, self._clear) # Método 3

        if text == 'D':
            self._connectButtonClicked(button, self._backspace) # Deleta o último caractere

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._configLeftOp, text) # Configura o operador
                )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)    
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        number = convertToNumber(displayText) * -1  # Converte o texto do display para número e inverte o sinal
        self.display.setText(str(number))
        self.display.setFocus()  # Foca no display para continuar digitando

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        # if buttonText == "=":
        #     self.display.setText(str(eval(self.display.text())))
        # else:
        #     self.display.insert(buttonText)

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus() # Foca no display para continuar digitando
    
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()  # Foca no display para continuar digitando

    @Slot()
    def _configLeftOp(self, text): # Quando selecionado o operador
        displayText = self.display.text() # Deverá ser o número _left
        self.display.clear() # Limpar o display
        self.display.setFocus() # Foca no display para continuar digitando 

        # Se selecionado o operador sem um número antes
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Selecione um número antes do operador')
            return
        
        # Se houver número na esquerda aguarde da direita, converte para convertToNumber não sobrescreve o esquerdo
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._op = text # Operador
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text() # Deverá ser o número _right

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Selecione um número para a direita')
            return
        
        self._right = convertToNumber(displayText) # Número da direita
        self._left: convertToNumber
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try: # result = eval(self.equation) Avalia a expressão matemática, mas com tratamento de erro
            if '^' in self.equation and isinstance(self._left, int | float):
                # result = eval(self.equation.replace('^', '**'))
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result)) # Converte o resultado para número
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero não é permitida')
        except OverflowError:
            self._showError('Resultado muito grande para ser calculado')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result 
        self._right = None
        self.display.setFocus() # Foca no display para continuar digitando

        if result == 'error':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace() # Deleta o último caractere do display
        self.display.setFocus() # Foca no display para continuar digitando
        
    def _makeDiaglog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDiaglog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()  # Foca no display para continuar digitando
        
        # msgBox.setInformativeText('Por favor, verifique os números e operadores inseridos.')
        # msgBox.setStandardButtons(msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel | msgBox.StandardButton.Ignore)
        # msgBox.button(msgBox.StandardButton.Cancel).setText('Cancelar')
        # msgBox.setStandardButtons(msgBox.StandardButton.Ok)
        

        # result = msgBox.exec()
        # if result == msgBox.StandardButton.Ok:
        #     print('Ok')
        # elif result == msgBox.StandardButton.Cancel:
        #     print('Cancel')
        # elif result == msgBox.StandardButton.Ignore:
        #     print('Ignore')
    
    def _showInfo(self, text):
        msgBox = self._makeDiaglog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()  # Foca no display para continuar digitando