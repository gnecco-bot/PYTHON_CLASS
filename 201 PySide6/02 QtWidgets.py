# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv) # Cria a aplicação

botao = QPushButton('Texto do botão') # Cria Botão
botao.setStyleSheet('font-size: 40px; color: Blue; Background-color: White') # Aceita aplicações em CSS
botao.show() # Adiciona o widget na hierarquia e exibe na janela o botão

app.exec() # O Execução da aplicação


