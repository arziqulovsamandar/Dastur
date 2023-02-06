from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

app = QApplication(sys.argv)
window = QWidget()
a = QLabel("Samandar", window)
b = QLabel("Arziqulov", window)
b1 = QLabel("Muhiddin o'g'li", window)
a.setGeometry(90,0, 200, 125)
b.setGeometry(90, 30, 200, 125)
b1.setGeometry(90, 60, 200, 125)
window.show()
app.exec_()

        