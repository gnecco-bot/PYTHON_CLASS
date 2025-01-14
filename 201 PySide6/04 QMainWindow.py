# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

def slot_exemple(status_bar):
    status_bar.showMessage('Foi executado')

# Status_Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar menssagem na barra')

# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))


window.show()
app.exec() # O loop da aplicação