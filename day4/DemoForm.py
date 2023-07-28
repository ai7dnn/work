# 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# form_class = uic.loadUiType("DemoForm.ui")[0]
# vs code 기본 작업 폴더 \work를 기준으로 찾음, 그래서 다음처럼 폴더를 적어주어야 함
# form_class = uic.loadUiType(".\\day4\\DemoForm.ui")[0]
# form_class = uic.loadUiType("day4/DemoForm.ui")[0]
form_class = uic.loadUiType("day4/DemoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫 번째 PyQt 데모")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()