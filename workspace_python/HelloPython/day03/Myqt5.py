import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic 




form_class = uic.loadUiType("myqt5.ui")[0]
class Myqt04(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.pb.clicked.connect(self.onClick)
        

    def onClick(self):
        for i in range(1,10) :
            j = int(self.le1.text())
            print(j)
            self.tb.append(f'{j} * {i} = {i*j}')
            
            
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = Myqt04()
    demoWindow.show() 
    app.exec_()