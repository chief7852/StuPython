import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic 




form_class = uic.loadUiType("myqt4.ui")[0]
class Myqt04(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.pb.clicked.connect(self.onClick)
        

    def onClick(self):
        num1 = self.le1.text()
        num2 = self.le2.text()
        aa = int(num1)
        bb = int(num2)
        sum = 0
        for i in range(aa,bb+1) :
            sum +=i
        self.le3.setText(str(sum))
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = Myqt04()
    demoWindow.show() 
    app.exec_()