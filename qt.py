import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import QStatusBar, QMainWindow, QApplication, QWidget,QHBoxLayout, qApp, QVBoxLayout, QPushButton, QSlider, QLCDNumber, QLabel, QAction
from PyQt5.QtGui import QIcon
class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.main_widget = FormWidget(self)
        self.setCentralWidget(self.main_widget)
        self.init_UI()

    def init_UI(self):
        exitAction = QAction(QIcon('exit.png'), '&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        sourceAction = QAction(QIcon('exit.png'), '&Источники', self)
        sourceAction.setShortcut('Ctrl+S')
        sourceAction.setStatusTip('Exit application')
        statusAction = QAction(QIcon('exit.png'), '&Статус', self)
        statusAction.setShortcut('Ctrl+S')
        statusAction.setStatusTip('Exit application')
        sellerAction = QAction(QIcon('exit.png'), '&Контрагент', self)
        sellerAction.setShortcut('Ctrl+S')
        sellerAction.setStatusTip('Exit application')
        kosguAction = QAction(QIcon('exit.png'), '&КОСГУ', self)
        kosguAction.setShortcut('Ctrl+S')
        kosguAction.setStatusTip('Exit application')
        yearAction = QAction(QIcon('exit.png'), '&Год', self)
        yearAction.setShortcut('Ctrl+S')
        yearAction.setStatusTip('Exit application')
        methodAction = QAction(QIcon('exit.png'), '&Метод', self)
        methodAction.setShortcut('Ctrl+S')
        methodAction.setStatusTip('Exit application')
        typesAction = QAction(QIcon('exit.png'), '&Тип', self)
        typesAction.setShortcut('Ctrl+S')
        typesAction.setStatusTip('Exit application')

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(exitAction)
        libMenu = menubar.addMenu('&Справочники')
        libMenu.addAction(statusAction)
        libMenu.addAction(sourceAction)
        libMenu.addAction(sellerAction)
        libMenu.addAction(kosguAction)
        libMenu.addAction(yearAction)
        libMenu.addAction(methodAction)
        libMenu.addAction(typesAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Central Widget')
        self.show()

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        hbox = QHBoxLayout()
        button_1 = QPushButton('Button 1', self)
        button_1.clicked.connect(self.buttonClicked)
        hbox.addWidget(button_1)
        button_2 = QPushButton('Button 2', self)
        button_2.clicked.connect(self.buttonClicked)
        hbox.addWidget(button_2)
        self.setLayout(hbox)
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Slider and LCD')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.parent.statusbar.showMessage(sender.text() + ' was clicked')

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(APP.exec_())
