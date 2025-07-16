import sys

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from buttons import ButtonsGrid
from styles import setupTheme

if __name__ == '__main__':
    # snake_case | PascalCase | camelCase | Estilos de nomeclaturas para variáveis e funções

    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # window.addWidgetToVLayout(temp_label('Label 1')) # Adiciona um Texto a janela

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display() # Texto que aparece digitado
    # display.setPlaceholderText('Digite algo') # Texto apagado de fundo
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # button1 = Button("Texto do botão") 
    # buttonsGrid.addWidget(Button('0'), 0, 0, 0) # linha / coluna / extender linha / extender coluna /  
    # button2 = Button("Texto do botão") 
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)
    # buttonsGrid.addWidget(Button('3'), 4, 0)


    # Executa tudo
    window.adjustFixedSize() # Ajusta o tamanho da janela e bloquea o redimencionamento
    window.show()
    app.exec()