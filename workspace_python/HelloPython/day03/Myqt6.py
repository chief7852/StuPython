import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic 
import random




form_class = uic.loadUiType("myqt6.ui")[0]
class Myqt04(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.pb.clicked.connect(self.onClick)
        

    def onClick(self):
        if random.randrange(1,3) == 1 :
            self.le1.setText("홀")
            self.checked()
        else :
            self.le1.setText("짝")
            self.checked()
        
            
    def checked(self):
        if self.le1.text()==self.le2.text():
            self.le3.setText("정답")
        else :
            self.le3.setText("오답")    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = Myqt04()
    demoWindow.show() 
    app.exec_()