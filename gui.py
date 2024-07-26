import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_gui import *
import qdarkstyle
import bug
from threading import Thread

class MyWindows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows,self).__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.run)
        self.flag = 0

    def run(self):
        if(self.flag == 0):
            self.protect()
            self.flag = 1
        else:
            self.stop()
            self.flag = 0

    def protect(self):
        self.button.setText("停止保护")
        thread1 = Thread(target=bug.protect, args=(self.text.toPlainText(), self.name.text()))
        thread1.start()

    def stop(self):
        self.button.setText("开始保护")
        bug.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    app.setStyleSheet(qdarkstyle.load_stylesheet(palette=qdarkstyle.LightPalette))
    window.show()
    sys.exit(app.exec_())
