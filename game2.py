from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
import random as r
ls=[str(i) for i in range(1,16)]
r.shuffle(ls)
class Tugma(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setFont(QFont("Times",40))
        self.setGeometry(x,y,100,100)
    def click(self,fun):
        self.clicked.connect(fun)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.begin()
    def font(self,ob):
        ob.setFont(QFont("Times",40))
    def begin(self):
        self.a1=Tugma("",self,50,50)
        self.a2=Tugma("",self,160,50)
        self.a3=Tugma("",self,270,50)
        self.a4=Tugma("",self,380,50)
        self.a5=Tugma("",self,50,160)
        self.a6=Tugma("",self,160,160)
        self.a7=Tugma("",self,270,160)
        self.a8=Tugma("",self,380,160)
        self.a9=Tugma("",self,50,270)
        self.a10=Tugma("",self,160,270)
        self.a11=Tugma("",self,270,270)
        self.a12=Tugma("",self,380,270)
        self.a13=Tugma("",self,50,380)
        self.a14=Tugma("",self,160,380)
        self.a15=Tugma("",self,270,380)
        self.a16=Tugma("",self,380,380)
        self.a16.hide()
        self.new=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11,self.a12,self.a13,self.a14,self.a15]
        for i in range(len(ls)):
            self.new[i].setText(ls[i])
        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)
        self.a7.click(self.A7)
        self.a8.click(self.A8)
        self.a9.click(self.A9)
        self.a10.click(self.A10)
        self.a11.click(self.A11)
        self.a12.click(self.A12)
        self.a13.click(self.A13)
        self.a14.click(self.A14)
        self.a15.click(self.A15)
        self.a16.click(self.A16)
    def test(self):
        win=QMessageBox(self)
        self.font(win)
        k=0
        for i in range(len(self.new)):
            if self.new[i].text()==str(i+1):
                k+=1
        if k==15:
            win.setText("YOU ARE WINNER!!!!!!")
            win.show()
    def A1(self):
        if self.a5.text()=="":
            self.a5.setText(self.a1.text())
            self.a1.setText("")
            self.a5.show()
            self.a1.hide()
        elif self.a2.text()=="":
            self.a2.setText(self.a1.text())
            self.a1.setText("")
            self.a2.show()
            self.a1.hide()
    def A2(self):
        if self.a1.text()=="":
            self.a1.setText(self.a2.text())
            self.a2.setText("")
            self.a1.show()
            self.a2.hide()
        elif self.a3.text()=="":
            self.a3.setText(self.a2.text())
            self.a2.setText("")
            self.a3.show()
            self.a2.hide()
        elif self.a6.text()=="":
            self.a6.setText(self.a2.text())
            self.a2.setText("")
            self.a6.show()
            self.a2.hide()
    def A3(self):
        if self.a2.text()=="":
            self.a2.setText(self.a3.text())
            self.a3.setText("")
            self.a2.show()
            self.a3.hide()
        elif self.a4.text()=="":
            self.a4.setText(self.a3.text())
            self.a3.setText("")
            self.a4.show()
            self.a3.hide()
        elif self.a7.text()=="":
            self.a7.setText(self.a3.text())
            self.a3.setText("")
            self.a7.show()
            self.a3.hide()
    def A4(self):
        if self.a3.text()=="":
            self.a3.setText(self.a4.text())
            self.a4.setText("")
            self.a3.show()
            self.a4.hide()
        elif self.a8.text()=="":
            self.a8.setText(self.a4.text())
            self.a4.setText("")
            self.a8.show()
            self.a4.hide()
    def A5(self):
        if self.a1.text()=="":
            self.a1.setText(self.a5.text())
            self.a5.setText("")
            self.a1.show()
            self.a5.hide()
        elif self.a9.text()=="":
            self.a9.setText(self.a5.text())
            self.a5.setText("")
            self.a9.show()
            self.a5.hide()
        elif self.a6.text()=="":
            self.a6.setText(self.a5.text())
            self.a5.setText("")
            self.a6.show()
            self.a5.hide()
    def A6(self):
        if self.a2.text()=="":
            self.a2.setText(self.a6.text())
            self.a6.setText("")
            self.a2.show()
            self.a6.hide()
        elif self.a5.text()=="":
            self.a5.setText(self.a6.text())
            self.a6.setText("")
            self.a5.show()
            self.a6.hide()
        elif self.a7.text()=="":
            self.a7.setText(self.a6.text())
            self.a6.setText("")
            self.a7.show()
            self.a6.hide()
        elif self.a10.text()=="":
            self.a10.setText(self.a6.text())
            self.a6.setText("")
            self.a10.show()
            self.a6.hide()
    def A7(self):
        if self.a3.text()=="":
            self.a3.setText(self.a7.text())
            self.a7.setText("")
            self.a3.show()
            self.a7.hide()
        elif self.a6.text()=="":
            self.a6.setText(self.a7.text())
            self.a7.setText("")
            self.a6.show()
            self.a7.hide()
        elif self.a8.text()=="":
            self.a8.setText(self.a7.text())
            self.a7.setText("")
            self.a8.show()
            self.a7.hide()
        elif self.a11.text()=="":
            self.a11.setText(self.a7.text())
            self.a7.setText("")
            self.a11.show()
            self.a7.hide()
    def A8(self):
        if self.a4.text()=="":
            self.a4.setText(self.a8.text())
            self.a8.setText("")
            self.a4.show()
            self.a8.hide()
        elif self.a7.text()=="":
            self.a7.setText(self.a8.text())
            self.a8.setText("")
            self.a7.show()
            self.a8.hide()
        elif self.a12.text()=="":
            self.a12.setText(self.a8.text())
            self.a8.setText("")
            self.a12.show()
            self.a8.hide()
    def A9(self):
        if self.a13.text()=="":
            self.a13.setText(self.a9.text())
            self.a9.setText("")
            self.a13.show()
            self.a9.hide()
        elif self.a10.text()=="":
            self.a10.setText(self.a9.text())
            self.a9.setText("")
            self.a10.show()
            self.a9.hide()
        elif self.a5.text()=="":
            self.a5.setText(self.a9.text())
            self.a9.setText("")
            self.a5.show()
            self.a9.hide()
    def A10(self):
        if self.a6.text()=="":
            self.a6.setText(self.a10.text())
            self.a10.setText("")
            self.a6.show()
            self.a10.hide()
        elif self.a9.text()=="":
            self.a9.setText(self.a10.text())
            self.a10.setText("")
            self.a9.show()
            self.a10.hide()
        elif self.a11.text()=="":
            self.a11.setText(self.a10.text())
            self.a10.setText("")
            self.a11.show()
            self.a10.hide()
        elif self.a14.text()=="":
            self.a14.setText(self.a10.text())
            self.a10.setText("")
            self.a14.show()
            self.a10.hide()
    def A11(self):
        if self.a7.text()=="":
            self.a7.setText(self.a11.text())
            self.a11.setText("")
            self.a7.show()
            self.a11.hide()
        elif self.a10.text()=="":
            self.a10.setText(self.a11.text())
            self.a11.setText("")
            self.a10.show()
            self.a11.hide()
        elif self.a12.text()=="":
            self.a12.setText(self.a11.text())
            self.a11.setText("")
            self.a12.show()
            self.a11.hide()
        elif self.a15.text()=="":
            self.a15.setText(self.a11.text())
            self.a11.setText("")
            self.a15.show()
            self.a11.hide()
    def A12(self):
        if self.a16.text()=="":
            self.a16.setText(self.a12.text())
            self.a12.setText("")
            self.a16.show()
            self.a12.hide()
        elif self.a11.text()=="":
            self.a11.setText(self.a12.text())
            self.a12.setText("")
            self.a11.show()
            self.a12.hide()
        elif self.a8.text()=="":
            self.a8.setText(self.a12.text())
            self.a12.setText("")
            self.a8.show()
            self.a12.hide()
    def A13(self):
        if self.a9.text()=="":
            self.a9.setText(self.a13.text())
            self.a13.setText("")
            self.a9.show()
            self.a13.hide()
        elif self.a14.text()=="":
            self.a14.setText(self.a13.text())
            self.a13.setText("")
            self.a14.show()
            self.a13.hide()
    def A14(self):
        if self.a13.text()=="":
            self.a13.setText(self.a14.text())
            self.a14.setText("")
            self.a13.show()
            self.a14.hide()
        elif self.a10.text()=="":
            self.a10.setText(self.a14.text())
            self.a14.setText("")
            self.a10.show()
            self.a14.hide()
        elif self.a15.text()=="":
            self.a15.setText(self.a14.text())
            self.a14.setText("")
            self.a15.show()
            self.a14.hide()
    def A15(self):
        if self.a16.text()=="":
            self.a16.setText(self.a15.text())
            self.a15.setText("")
            self.a16.show()
            self.a15.hide()
        elif self.a11.text()=="":
            self.a11.setText(self.a15.text())
            self.a15.setText("")
            self.a11.show()
            self.a15.hide()
        elif self.a14.text()=="":
            self.a14.setText(self.a15.text())
            self.a15.setText("")
            self.a14.show()
            self.a15.hide()
    def A16(self):
        if self.a15.text()=="":
            self.a15.setText(self.a16.text())
            self.a16.setText("")
            self.a15.show()
            self.a16.hide()
        elif self.a12.text()=="":
            self.a12.setText(self.a16.text())
            self.a16.setText("")
            self.a12.show()
            self.a16.hide()
        self.test()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())