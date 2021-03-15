import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtWidgets 





form_class = uic.loadUiType("myqt8.ui")[0]
class Myqt8(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(0,10):
            exec(f'self.btn{i}.clicked.connect(self.onEvent)')
        self.btnCall.clicked.connect(self.myCall)
 
    def onEvent(self):
        print(self.sender().text())
        txt_old = self.le1.text()
        txt_new = self.sender().text()
        self.le1.setText(txt_old+txt_new)
        
    def myCall(self):
        txt_call = self.le1.text()
        QtWidgets.QMessageBox.about(self,"Calling", txt_call)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = Myqt8()
    demoWindow.show() 
    app.exec_()