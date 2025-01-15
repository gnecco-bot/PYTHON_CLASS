# O básico sobre Signal e Slots (eventos e documentação)

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

@Slot()
def slot_exemple(status_bar):
    def inner():
        status_bar.showMessage("O meui slot foi executado")
    return inner

@Slot()
def outro_slot(checked):
    print('Está Marcado?', checked)

@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

# Status_Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar menssagem na barra')

# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_exemple(status_bar))

segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True) # Torna marcavel uma opção do menubar
segunda_acao.toggled.connect(outro_slot) # Retorna True ou False se não estiver marcado
segunda_acao.hovered.connect(terceiro_slot(segunda_acao)) # Retorna True ou False se não estiver marcado

botao1.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec() # O loop da aplicação