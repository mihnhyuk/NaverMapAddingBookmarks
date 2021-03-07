import sys

from PyQt5.QtWidgets import QFileDialog, QApplication, QInputDialog, QMessageBox
from webauto import webauto
import csvio
import gui


class MyApp(gui.MyApp):
    addresses = None
    ID = None
    PW = None
    logged_in = False
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = open(fname[0], 'r')
                self.addresses = csvio.get_file(data)

    def log_in_btn(self):
        self.ID, ok1 = QInputDialog.getText(self, 'Input Dialog', 'Enter your ID:')
        self.PW, ok2 = QInputDialog.getText(self, 'Input Dialog', 'Enter your PW:')
        webauto.login.log_in(webauto.driver, self.ID, self.PW)
        self.logged_in = True
    def start_bookmark(self):

        if self.logged_in:
            webauto.add_fav_inNavermap(self.addresses)
        else:
            reply = QMessageBox()
            reply.setText("로그인 후 이용해주세요")
            reply.setStandardButtons(QMessageBox.Ok)
            reply.exec()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
