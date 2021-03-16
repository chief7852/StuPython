'''
Created on 11 Mar 2021

@author: shane
'''

import sys

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication, QPushButton, QIcon, QSize


form_class = uic.loadUiType("mygo.ui")[0]



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
            ]
        self.arr2pb = []
        self.turn = True
    
        iconSize = 40
        self.size = 10
        for i in range(0,self.size):
            line = []
            for j in range(0,self.size):
                pb = QPushButton(self)
                pb.setIcon(QIcon('0.png'))
                pb.setIconSize(QSize(iconSize,iconSize))
                pb.setGeometry(i*iconSize,j*iconSize,iconSize,iconSize)
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{0},{1}".format(i,j))
                line.append(pb)
            self.arr2pb.append(line)
        
        self.pb_reset.clicked.connect(self.reset) 
        self.myrender()
    
    def getUp(self,i,j,int_wb):
        cnt = 0 
        while(i< self.size and j< self.size) :
            if(self.arr2D[i][j] == int_wb):
                cnt += 1
                j -= 1
            else: break
        return cnt

   
    def myrender(self):
        if(self.turn):
            self.turnBtn.setIcon(QIcon('2.png')) 
        else:
            self.turnBtn.setIcon(QIcon('1.png')) 
            
        for i in range(0,10):
            for j in range(0,10):
                if(self.arr2D[i][j] == 0):
                    self.arr2pb[i][j].setIcon(QIcon('0.png'))         
                if(self.arr2D[i][j] == 1):
                    self.arr2pb[i][j].setIcon(QIcon('1.png'))         
                elif(self.arr2D[i][j] == 2):
                    self.arr2pb[i][j].setIcon(QIcon('2.png'))  
                           
    def myclick(self):
        arr = self.sender().toolTip().split(",")
        i = int(arr[0])
        j = int(arr[1])
        
        if(self.arr2D[i][j] == 0):
            self.arr2D[i][j] = 2 if self.turn else 1
            self.myrender()
            up = self.getUp(i,j,2 if self.turn else 1)
            print(up)
            
            if( up == 5):
                QtWidgets.QMessageBox.about(self,"message","흑 승" if self.turn else "백 승")
            
            self.turn = not self.turn
    
    def reset(self):
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
            ]
        self.turn = 2
        self.myrender()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    
    