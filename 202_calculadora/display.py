from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    """Classe que representa o display da calculadora, onde os números e operações são exibidos."""
    eqPressed = Signal()  # Sinal para requisitar a equação
    delpressed = Signal()  # Sinal para requisitar a exclusão do último caractere
    clearPressed = Signal()  # Sinal para requisitar a limpeza do display
    imputPressed = Signal(str)  # Sinal para requisitar a entrada de texto no display
    operatorpressed = Signal(str)  # Sinal para requisitar a operação matemática

    def __init__(self, *args, **kwargs):
        super().__init__( *args, *kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)] # list comprehension 
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;') # Tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # Tamanho da altura do display
        self.setMinimumWidth(MINIMUM_WIDTH) # Minimo de largura do display
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # Alinhamendo do texto a direita da display
        self.setTextMargins(*margins) # Margem de 15px nos 4 lados

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()  # Remove espaços em branco no início e no fim
        key = event.key()
        KEYS = Qt.Key

        isEnter = key == KEYS.Key_Enter or key == KEYS.Key_Return or key == KEYS.Key_Equal
        isDelete = key == KEYS.Key_Backspace or key == KEYS.Key_Delete or key == KEYS.Key_D
        isEsc = key == KEYS.Key_Escape or key == KEYS.Key_C #'C' é usado para limpar o display
        isOperator = key in (KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Asterisk, KEYS.Key_Slash, KEYS.Key_P)  # Operadores matemáticos

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()
    
        if isDelete:
            self.delpressed.emit()
            return event.ignore()
        
        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
                
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorpressed.emit(text)
            return event.ignore()
        
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.imputPressed.emit(text)
            return event.ignore()