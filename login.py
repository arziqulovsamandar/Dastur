from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableWidget,QTableWidgetItem,QMessageBox
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
            database="T"
        )
        self.cur=self.mydb.cursor()
        self.setWindowTitle("PyQt5+MySQL")
        self.setGeometry(100,100,600,500)
        self.createDB()
        self.insert_table()
        self.start()
        self.show()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",20))
        ob.move(x,y)
    def start(self):
        self.login=QPushButton("Log in",self)
        self.font(self.login,50,50)
        self.login.clicked.connect(self.Login)
        self.login.show()

        self.singin=QPushButton("Sing in",self)
        self.font(self.singin,50,110)
        self.singin.clicked.connect(self.Singin)
        self.singin.show()

        self.Login=QLabel("Login:",self)
        self.font(self.Login,50,50)
        self.Login.hide()

        self.Password=QLabel("Password:",self)
        self.font(self.Password,50,110)
        self.Password.hide()

        self.log_e=QLineEdit(self)
        self.font(self.log_e,220,50)
        self.log_e.hide()

        self.pass_e=QLineEdit(self)
        self.font(self.pass_e,220,110)
        self.pass_e.hide()

        self.ok=QPushButton("OK",self)
        self.font(self.ok,450,170)
        self.ok.clicked.connect(self.Ok)
        self.ok.hide()

        self.can=QPushButton("Cancel",self)
        self.font(self.can,330,170)
        self.can.clicked.connect(self.Can)
        self.can.hide()



        self.ok2=QPushButton("OK",self)
        self.font(self.ok2,450,230)
        self.ok2.clicked.connect(self.Ok2)
        self.ok2.hide()

        self.can2=QPushButton("Cancel",self)
        self.font(self.can2,330,230)
        self.can2.clicked.connect(self.Can2)
        self.can2.hide()

        self.sponsor=QLabel("Sponsor:",self)
        self.font(self.sponsor,50,170)
        self.sponsor.hide()

        self.spon_e=QLineEdit(self)
        self.font(self.spon_e,220,170)
        self.spon_e.hide()

        self.Password2=QLabel("Password:",self)
        self.font(self.Password2,50,110)
        self.Password2.hide()

        self.pass_e2=QLineEdit(self)
        self.font(self.pass_e2,220,110)
        self.pass_e2.hide()



        self.ok3=QPushButton("OK",self)
        self.font(self.ok3,450,170)
        self.ok3.clicked.connect(self.Ok3)
        self.ok3.hide()

        self.can3=QPushButton("Cancel",self)
        self.font(self.can3,330,170)
        self.can3.clicked.connect(self.Can3)
        self.can3.hide()

        self.back=QPushButton("Back",self)
        self.font(self.back,100,100)
        self.back.clicked.connect(self.Back)
        self.back.hide()
    def Login(self):
        self.login.hide()
        self.singin.hide()
        self.Login.show()
        self.Password.show()
        self.log_e.show()
        self.pass_e.show()
        self.ok.show()
        self.can.show()
    def Can(self):
        self.login.show()
        self.singin.show()
        self.Login.hide()
        self.Password.hide()
        self.log_e.hide()
        self.pass_e.hide()
        self.ok.hide()
        self.can.hide()
        self.log_e.clear()
        self.pass_e.clear()
    def Ok(self):
        a1=str(self.log_e.text())
        a2=str(self.pass_e.text())
        self.cur.execute("select * from User")
        text=self.cur.fetchall()
        for i in range(len(text)):
            if text[i][0]==a1 and text[i][1]==a2:
                miniwindow=QMessageBox(self)
                miniwindow.setText("Siz tizimga kirdingiz")
                miniwindow.show()
        
    def createDB(self):
        self.cur.execute("Create Table if not exists User(login Varchar(50), password varchar(50))")
        self.mydb.commit()
    def insert_table(self):
        print(1)
        self.cur.execute("insert into User values(%s, %s)",
                                ["admin", "1234"])
        self.mydb.commit()
    def Singin(self):
        self.login.hide()
        self.singin.hide()
        self.Login.show()
        self.Password.show()
        self.log_e.show()
        self.pass_e.show()
        self.can2.show()
        self.ok2.show()
        self.sponsor.show()
        self.spon_e.show()
    def Can2(self):
        self.login.show()
        self.singin.show()
        self.Login.hide()
        self.Password.hide()
        self.log_e.hide()
        self.pass_e.hide()
        self.ok2.hide()
        self.can2.hide()
        self.spon_e.hide()
        self.sponsor.hide()
        self.log_e.clear()
        self.pass_e.clear()
    def Ok2(self):
        s1=str(self.spon_e.text())
        self.cur.execute("select * from User")
        text=self.cur.fetchall()
        for i in range(len(text)):
            if text[i][0]==s1:
                self.Login.hide()
                self.Password.hide()
                self.log_e.hide()
                self.pass_e.hide()
                self.can2.hide()
                self.ok2.hide()
                self.can3.show()
                self.ok3.show()
                self.sponsor.hide()
                self.spon_e.hide()
                self.Password2.show()
                self.pass_e2.show()
    def Can3(self):
        self.login.hide()
        self.singin.hide()
        self.Login.show()
        self.Password.show()
        self.log_e.show()
        self.pass_e.show()
        self.can2.show()
        self.ok2.show()
        self.sponsor.show()
        self.spon_e.show()
        self.pass_e2.hide()
        self.Password2.hide()
        self.ok3.hide()
        self.can3.hide()
        self.log_e.clear()
        self.pass_e.clear()
        self.spon_e.clear()
    def Ok3(self):
        a1=str(self.log_e.text())
        a2=str(self.pass_e.text())
        s1=str(self.spon_e.text())
        s2=str(self.pass_e2.text())
        self.cur.execute("select * from User")
        text=self.cur.fetchall()
        for i in range(len(text)):
            if text[i][0]==s1 and text[i][1]==s2:
                self.cur.execute("Insert Into User values(%s,%s)",(a1,a2))
                self.mydb.commit()
                self.log_e.clear()
                self.pass_e.clear()
                self.spon_e.clear()
                self.pass_e2.clear()
                miniwindow=QMessageBox(self)
                miniwindow.setText("Ro`yxatdan o`tish muvofaqiyatli yakunlandi")
                miniwindow.show()
                self.ok3.hide()
                self.can3.hide()
                self.pass_e2.hide()
                self.Password2.hide()
                self.login.show()
                self.singin.show()
                break
            if i==len(text)-1:
                self.back.show()
                self.pass_e2.hide()
                self.Password2.hide()
                self.can3.hide()
                self.ok3.hide()

    def Back(self):
        self.login.hide()
        self.singin.hide()
        self.Login.show()
        self.Password.show()
        self.log_e.show()
        self.pass_e.show()
        self.can2.show()
        self.ok2.show()
        self.sponsor.show()
        self.spon_e.show()
        self.pass_e2.hide()
        self.Password2.hide()
        self.ok3.hide()
        self.can3.hide()
        self.back.hide()
        self.pass_e2.clear()
win=Window()
sys.exit(app.exec_())




