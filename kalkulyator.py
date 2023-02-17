'''from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QTextEdit,QPushButton
from PyQt5.QtGui import QFont

import sys

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Kalkulyator")
window.setGeometry(20,20,360,360)


y=QLabel("0",window)
y.setFont(QFont("times",24))
y.move(10,100)
q=0
add=QPushButton("1",window)
add.setFont(QFont("times",24))
add.move(10,150)
def run():
    a=1
    q=str(q)
    q+=1
    a=str(a)
    y.setText(a)
    y.adjustSize()  
add.clicked.connect(run)

add1=QPushButton("2",window)
add1.setFont(QFont("times",24))
add1.move(95,150)
def run():
    a=2
    q+=2
    a=str(a)
    y.setText(a)
    y.adjustSize()
add1.clicked.connect(run)

add3=QPushButton("3",window)
add3.setFont(QFont("times",24))
add3.move(180,150)
def run():
    a=3
    q+=3
    a=str(a)
    y.setText(a)
    y.adjustSize()
add3.clicked.connect(run)

add4=QPushButton("4",window)
add4.setFont(QFont("times",24))
add4.move(10,200)
def run():
    a=4
    q+=4
    a=str(a)
    y.setText(a)
    y.adjustSize()  
add4.clicked.connect(run)

add5=QPushButton("5",window)
add5.setFont(QFont("times",24))
add5.move(95,200)
def run():
    a=5
    q+=5
    a=str(a)
    y.setText(a)
    y.adjustSize()
add5.clicked.connect(run)
    
add6=QPushButton("6",window)
add6.setFont(QFont("times",24))
add6.move(180,200)
def run():
    a=6
    q+=6
    a=str(a)
    y.setText(a)
    y.adjustSize()
add6.clicked.connect(run)

add7=QPushButton("7",window)
add7.setFont(QFont("times",24))
add7.move(10,250)
def run():
    a=7
    q+=7
    a=str(a)
    y.setText(a)
    y.adjustSize()
add7.clicked.connect(run)

add8=QPushButton("8",window)
add8.setFont(QFont("times",24))
add8.move(95,250)
def run():
    a=8
    q+=8
    a=str(a)
    y.setText(a)
    y.adjustSize()
add8.clicked.connect(run)

add9=QPushButton("9",window)
add9.setFont(QFont("times",24))
add9.move(180,250)
def run():
    a=9
    q+=9
    a=str(a)
    y.setText(a)
    y.adjustSize()
add9.clicked.connect(run)

addc=QPushButton("C",window)
addc.setFont(QFont("times",24))
addc.move(10,300)
def run():
    a=0
    q=0
    a=str(a)
    y.setText(a)
    y.adjustSize()
addc.clicked.connect(run)

adda=QPushButton("+",window)
adda.setFont(QFont("times",24))
adda.setGeometry(265,150,85,75)
def run():
    a="+"
    q='+'
    y.setText(a)
    y.adjustSize()
adda.clicked.connect(run)

addd=QPushButton("-",window)
addd.setFont(QFont("times",24))
addd.setGeometry(265,225,85,75)
def run():
    a='-'
    q='-'
    y.setText(a)
    y.adjustSize()
addd.clicked.connect(run)


addd2=QPushButton("=",window)
addd2.setFont(QFont("times",24))
addd2.setGeometry(95,300,255,50)
def run():
    a='='
    q='='
    a=str(a)
    y.setText(a)
    y.adjustSize()
addd2.clicked.connect(run)
q=str(q)
y.setText(q)
y.adjustSize()
window.show()
app.exec_()'''
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Tugma(QPushButton):
    def __init_subclass(cls):
        return super().__init_subclass()
    def font(self,x,y):
        self.setFont(QFont("Times",30))
        self.setGeometry(x,y,50,50)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-UYGA VAZIFA")
        self.setGeometry(250,250,500,600)
        self.start()
        self.show()
    def start(self):
        self.a1=Tugma("1",self)
        self.a1.font(50,50)
        self.a2=Tugma("2",self)
        self.a2.font(105,50)
        self.a3=Tugma("3",self)
        self.a3.font(160,50)
        self.a4=Tugma("4",self)
        self.a4.font(50,105)
        self.a5=Tugma("5",self)
        self.a5.font(105,105)
        self.a6=Tugma("6",self)
        self.a6.font(160,105)
        self.a7=Tugma("7",self)
        self.a7.font(50,160)
        self.a8=Tugma("8",self)
        self.a8.font(105,160)
        self.a9=Tugma("9",self)
        self.a9.font(160,160)
        self.c=Tugma("C",self)
        self.c.font(50,215)
        self.nol=Tugma("0",self)
        self.nol.font(105,215)
        self.equal=Tugma("=",self)
        self.equal.font(160,215)
        self.plus=Tugma("+",self)
        self.plus.font(215,50)
        self.minus=Tugma("-",self)
        self.minus.font(215,105)
        self.multy=Tugma("*",self)
        self.multy.font(215,160)
        self.divide=Tugma("/",self)
        self.divide.font(215,215)
        self.result=QLineEdit(self)
        self.result.setPlaceholderText("0")
        self.result.setFont(QFont("Times",30))
        self.result.setGeometry(50,270,215,50)
        self.a1.clicked.connect(self.A1)
        self.a2.clicked.connect(self.A2)
        self.a3.clicked.connect(self.A3)
        self.a4.clicked.connect(self.A4)
        self.a5.clicked.connect(self.A5)
        self.a6.clicked.connect(self.A6)
        self.a7.clicked.connect(self.A7)
        self.a8.clicked.connect(self.A8)
        self.a9.clicked.connect(self.A9)
        self.nol.clicked.connect(self.Nol)
        self.plus.clicked.connect(self.Plus)
        self.minus.clicked.connect(self.Minus)
        self.multy.clicked.connect(self.Multy)
        self.divide.clicked.connect(self.Divide)
        self.equal.clicked.connect(self.Equal)
        self.c.clicked.connect(self.Clear)
    def A1(self):
        self.result.setText(self.result.text()+self.a1.text())
    def A2(self):
        self.result.setText(self.result.text()+self.a2.text())
    def A3(self):
        self.result.setText(self.result.text()+self.a3.text())
    def A4(self):
        self.result.setText(self.result.text()+self.a4.text())
    def A5(self):
        self.result.setText(self.result.text()+self.a5.text())
    def A6(self):
        self.result.setText(self.result.text()+self.a6.text())
    def A7(self):
        self.result.setText(self.result.text()+self.a7.text())
    def A8(self):
        self.result.setText(self.result.text()+self.a8.text())
    def A9(self):
        self.result.setText(self.result.text()+self.a9.text())
    def Nol(self):
        self.result.setText(self.result.text()+self.nol.text())
    def Plus(self):
        self.result.setText(self.result.text()+self.plus.text())
    def Minus(self):
        self.result.setText(self.result.text()+self.minus.text())
    def Multy(self):
        self.result.setText(self.result.text()+self.multy.text())
    def Divide(self):
        self.result.setText(self.result.text()+self.divide.text())
    def Equal(self):
        self.result.setText(str(eval(self.result.text())))
    def Clear(self):
        self.result.setText("")
win=Window()
app.exec_()