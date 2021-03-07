import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, \
    QInputDialog, QLineEdit, QFileDialog, QTextEdit, QVBoxLayout, QGridLayout, QLabel


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f = None

        textintro = QLabel('welcome',self)
        textintro.setAlignment(Qt.AlignCenter)
        textintro.setFont(QtGui.QFont("",20))


        widget = QWidget(self)
        gridlayout = QGridLayout(widget)
        btn1 = QPushButton('open file', self)
        btn1.setText('파일 찾기')
        btn1.clicked.connect(self.openFile)

        btn2 = QPushButton('login', self)
        btn2.setText('로그인')
        btn2.clicked.connect(self.log_in_btn)

        btn3 = QPushButton('start', self)
        btn3.setText('즐겨찾기 추가')
        btn3.clicked.connect(self.start_bookmark)

        gridlayout.addWidget(textintro, 0, 0)
        gridlayout.addWidget(btn1, 1,0)
        gridlayout.addWidget(btn2, 1,1)
        gridlayout.addWidget(btn3, 2,0)

        openFileAction = QAction(QIcon('oepn.png'), 'Open', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open New File')
        openFileAction.triggered.connect(self.openFile)

        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFileAction)


        self.setCentralWidget(widget)


        self.resize(500,350)
        self.center()
        self.show()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = open(fname[0], 'r')
                self.textEdit.setText(data)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def log_in_btn(self):
        pass
    def start_bookmark(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


