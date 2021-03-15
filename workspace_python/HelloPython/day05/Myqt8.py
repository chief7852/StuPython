import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtWidgets 





form_class = uic.loadUiType("myqt8.ui")[0]
class Myqt8(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = Myqt8()
    demoWindow.show() 
    app.exec_()