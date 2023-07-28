# web1.py
# 클롤링을 하기 위한 선언

from bs4 import BeautifulSoup

# 페이지를 로딩(메소드 체인)
page = open('D:\\hskang\\work\\day4\\test01.html', 'rt', encoding='utf-8').read()
# page = open(r'D:\hskang\work\day4\test01.html', 'rt', encoding='utf-8').read()
# 검색이 용이한 객체 생성, 'html.parser': 상수처럼 사용
soup = BeautifulSoup(page, 'html.parser')
# 페이지 보기
# print(soup.prettify())

# # <p> 전체를 검색
# print(soup.find_all('p'))
# print(soup.find('p'))
# <p class='outer=text'> 조건 검색
# print(soup.find_all('p', class_='outer-text'))
# attrs: Atrributes(속성들)
# print(soup.find_all('p', attrs={'class': 'outer-text'}))
# print(soup.find_all('p', attrs={'class': 'outer-text first-'}))
# print(soup.find_all(id='first'))
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n', "")
    print(title)

