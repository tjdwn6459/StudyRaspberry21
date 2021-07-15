## QT5 베으스 프레임 소스 
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
#button = QPushButton("click me")


#button.show()
win = MyWindow()
win.show()

app.exec_()