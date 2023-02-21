from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableWidget,QTableWidgetItem,QMessageBox,QTextEdit
from PyQt5.QtGui import QFont
import mysql.connector, sys

app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Telegram"
        )
        self.cur=self.mydb.cursor()
        self.setWindowTitle("PyQt5+MySQL")
        self.setGeometry(100,100,800,800)
        #self.createDB()
        #self.insert_table()
        self.start()
        self.show()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",20))
        ob.move(x,y)
    def start(self):
        self.user=QLabel("User:",self)
        self.font(self.user,50,60)

        self.pasword=QLabel("password:",self)
        self.font(self.pasword,50,120)

        self.user1=QLineEdit(self)
        self.font(self.user1,180,50)


        self.pasword1=QLineEdit(self)
        self.font(self.pasword1,180,110)

        self.can=QPushButton("Cancel",self)
        self.font(self.can,200,450)
        self.can.clicked.connect(self.Can)
        self.can.hide()

        self.whom=QLabel("Whom",self)
        self.font(self.whom,50,60)
        self.whom.hide()

        self.send1=QLineEdit(self)
        self.font(self.send1,150,50)
        self.send1.hide()

        self.output=QLabel("Output text",self)
        self.font(self.output,400,150)
        self.output.hide()

        self.out=QTextEdit(self)
        self.font(self.out,400,200)
        self.out.hide()

        self.output1=QLabel("output text",self)
        self.font(self.output1,400,150)
        self.output1.hide()

        self.out1=QTextEdit(self)
        self.font(self.out1,400,200)
        self.out1.hide()

        self.input=QLabel("Input text",self)
        self.font(self.input,50,150)
        self.input.hide()

        self.inp=QTextEdit(self)
        self.font(self.inp,50,200)
        self.inp.hide()
        #self.sen=QPushButton("Send",self)
        #self.font(self.sen,100,300)
        #self.sen.clicked.connect(self.sen)
        #self.sen.hide()
        self.lsend=QPushButton("Send",self)
        self.font(self.lsend,100,450)
        self.lsend.clicked.connect(self.Send)
        self.lsend.hide()



        self.ok=QPushButton("OK",self)
        self.font(self.ok,200,200)
        self.ok.clicked.connect(self.Add1)
    def Add1(self):
        #self.hide()
        if self.user1.text()=="admin" and self.pasword1.text()=='1234':
           self.ok.hide()
           self.pasword1.hide()
           self.user1.hide()
           self.pasword.hide()
           self.user.hide()
           self.whom.show()
           self.send1.show()
           self.output.show()
           self.out.show()
           self.input.show()
           self.inp.show()
           self.lsend.show()
           self.can.show()
        elif self.user1.text()=="user12" and self.pasword1.text()=='4321':
           self.ok.hide()
           self.pasword1.hide()
           self.user1.hide()
           self.pasword.hide()
           self.user.hide()
           self.whom.show()
           self.send1.show()
           self.output1.show()
           self.out1.show()
           self.input.show()
           self.inp.show()
           self.lsend.show()
           self.can.show()
    def Can(self):
        self.ok.show()
        self.pasword1.show()
        self.user1.show()
        self.pasword.show()
        self.user.show()
        self.whom.hide()
        self.send1.hide()
        self.output.hide()
        self.output1.hide()
        self.out.hide()
        self.out1.hide()
        self.input.hide()
        self.inp.hide()
        self.lsend.hide()
        self.send1.clear()
        self.inp.clear()
        self.can.hide()
        self.user1.clear()
        self.pasword1.clear()
    def Send(self):
        if self.send1.text()=='admin':
            
            print(1)
            
            a=self.inp.toPlainText()
           
            print(a)
            a1=self.send1.text()
            a2=self.inp.toPlainText()
            self.cur.execute("INSERT INTO chat VALUES(%s,%s)",(a1,a2))
            self.mydb.commit()
            self.out.setText(a)
            self.out.adjustSize()
            self.send1.clear()
            self.inp.clear()
        elif self.send1.text()=='user12':
        
            print(2)
            
            a=self.inp.toPlainText()
            print(a)
            a1=self.send1.text()
            a2=self.inp.toPlainText()
            self.cur.execute("INSERT INTO chat VALUES(%s,%s)",(a1,a2))
            self.mydb.commit()
            
            self.out1.setText(a)
            self.out1.adjustSize()
            self.send1.clear()
            self.inp.clear()



win=Window()
sys.exit(app.exec_())