# DemoForm2.py
# DemoForm2.ui

import requests
from bs4 import BeautifulSoup

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# form_class = uic.loadUiType("DemoForm.ui")[0]
# vs code 기본 작업 폴더 \work를 기준으로 찾음, 그래서 다음처럼 폴더를 적어주어야 함
# form_class = uic.loadUiType(".\\day4\\DemoForm.ui")[0]
# form_class = uic.loadUiType("day4/DemoForm2.ui")[0]
form_class = uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫 번째 PyQt 데모")
    
    # 슬롯메소드 
    def firstClick(self):

        # 페이지를 로딩(메소드 체인)
        url = 'https://www.daangn.com/'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', attrs={'class': 'card-desc'})

        # 파일에 저장
        f = open('D:\\hskang\\work\\day4\\daangn.txt', 'wt', encoding='utf-8')
        for post in posts:
            title = post.find('h2', attrs={'class': 'card-title'})
            price = post.find('div', attrs={'class': 'card-price'})
            addr = post.find('div', attrs={'class': 'card-region-name'})
            title = title.text.strip()
            price = price.text.strip()
            addr = addr.text.strip()
            title = title.replace('\n', '')
            price = price.replace('\n', '')
            addr = addr.replace('\n', '')
            print(f'{title}, {price}, {addr}')
            f.write(f'{title}, {price}, {addr}\n')

        f.close()

        self.label.setText('당근마켓 크롤링 완료')
    def secondClick(self):
        self.label.setText('두번째 버튼 클릭')
    def thirdClick(self):
        self.label.setText('세번째 버튼 클릭~~~')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()