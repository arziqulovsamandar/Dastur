from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QRadioButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Tugma(QPushButton):
    def init_subclass(cls):
        return super().init_subclass()
    def font(self,x,y):
        self.setFont(QFont("Times",30))
        self.adjustSize()
        self.setGeometry(x,y,50,50)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.t=""
        self.setWindowTitle("TIC-TAC-TOE")
        self.setGeometry(250,250,400,500)
        self.start()
        self.show()
    def run(self):
        self.x.hide()
        self.o.hide()
        self.ok.hide()
        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.a4.show()
        self.a5.show()
        self.a6.show()
        self.a7.show()
        self.a8.show()
        self.a9.show()
        if self.x.isChecked():
            self.t="X"
        elif self.o.isChecked():
            self.t="O"
    def start(self):
        self.x=QRadioButton("X",self)
        self.x.setFont(QFont("Times",30))
        self.x.move(20,20)
        
        self.o=QRadioButton("O",self)
        self.o.setFont(QFont("Times",30))
        self.o.move(70,20)
        
        self.ok=Tugma("OK",self)
        self.ok.setFont(QFont("Times",25))
        self.ok.move(40,70)
        self.ok.clicked.connect(self.run)

        self.a1=Tugma("",self)
        self.a1.font(50,50)
        self.a1.clicked.connect(self.A1)

        self.a2=Tugma("",self)
        self.a2.font(105,50)
        self.a2.clicked.connect(self.A2)

        self.a3=Tugma("",self)
        self.a3.font(160,50)
        self.a3.clicked.connect(self.A3)

        self.a4=Tugma("",self)
        self.a4.font(50,105)
        self.a4.clicked.connect(self.A4)

        self.a5=Tugma("",self)
        self.a5.font(105,105)
        self.a5.clicked.connect(self.A5)

        self.a6=Tugma("",self)
        self.a6.font(160,105)
        self.a6.clicked.connect(self.A6)

        self.a7=Tugma("",self)
        self.a7.font(50,160)
        self.a7.clicked.connect(self.A7)

        self.a8=Tugma("",self)
        self.a8.font(105,160)
        self.a8.clicked.connect(self.A8)

        self.a9=Tugma("",self)
        self.a9.font(160,160)
        self.a9.clicked.connect(self.A9)
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.a4.hide()
        self.a5.hide()
        self.a6.hide()
        self.a7.hide()
        self.a8.hide()
        self.a9.hide()
    def change(self):
        if self.t=="X":
            self.t="O"
        elif self.t=="O":
            self.t="X"
    def reset(self):
        self.x.show()
        self.o.show()
        self.ok.show()
        self.a1.hide()
        self.a1.setText("")
        self.a2.hide()
        self.a2.setText("")
        self.a3.hide()
        self.a3.setText("")
        self.a4.hide()
        self.a4.setText("")
        self.a5.hide()
        self.a5.setText("")
        self.a6.hide()
        self.a6.setText("")
        self.a7.hide()
        self.a7.setText("")
        self.a8.hide()
        self.a8.setText("")
        self.a9.hide()
        self.a9.setText("")
    def winner(self):
        win=QMessageBox(self)
        if self.a1.text()!="" and self.a1.text()==self.a2.text() and self.a1.text()==self.a3.text():
            win.setText(self.a1.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a1.text()!="" and self.a1.text()==self.a4.text() and self.a1.text()==self.a7.text():
            win.setText(self.a1.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a1.text()!="" and self.a1.text()==self.a5.text() and self.a1.text()==self.a9.text():
            win.setText(self.a1.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a2.text()!="" and self.a2.text()==self.a5.text() and self.a2.text()==self.a8.text():
            win.setText(self.a2.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a3.text()!="" and self.a3.text()==self.a6.text() and self.a3.text()==self.a9.text():
            win.setText(self.a3.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a3.text()!="" and self.a3.text()==self.a5.text() and self.a3.text()==self.a7.text():
            win.setText(self.a3.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a4.text()!="" and self.a4.text()==self.a5.text() and self.a4.text()==self.a6.text():
            win.setText(self.a4.text()+" WINNER!!!!")
            win.show()
            self.reset()
        elif self.a7.text()!="" and self.a7.text()==self.a8.text() and self.a7.text()==self.a9.text():
            win.setText(self.a7.text()+" WINNER!!!!")
            win.show()
            self.reset()
    def A1(self):
        if self.a1.text()=="":
            self.a1.setText(self.t)
            self.change()
        self.winner()
    def A2(self):
        if self.a2.text()=="":
            self.a2.setText(self.t)
            self.change()
        self.winner()
    def A3(self):
        if self.a3.text()=="":
            self.a3.setText(self.t)
            self.change()
        self.winner()
    def A4(self):
        if self.a4.text()=="":
            self.a4.setText(self.t)
            self.change()
        self.winner()
    def A5(self):
        if self.a5.text()=="":
            self.a5.setText(self.t)
            self.change()
        self.winner()
    def A6(self):
        if self.a6.text()=="":
            self.a6.setText(self.t)
            self.change()
        self.winner()
    def A7(self):
        if self.a7.text()=="":
            self.a7.setText(self.t)
            self.change()
        self.winner()
    def A8(self):
        if self.a8.text()=="":
            self.a8.setText(self.t)
            self.change()
        self.winner()
    def A9(self):
        if self.a9.text()=="":
            self.a9.setText(self.t)
            self.change()
        self.winner()
win=Window()
app.exec_()