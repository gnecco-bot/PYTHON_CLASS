from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        
        # Título da janela
        self.setWindowTitle('Calculadora')

    # Ajusta o tamanho da janela e bloquea o redimencionamento
    def adjustFixedSize(self): 
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    # Adiciona interação a janela
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
