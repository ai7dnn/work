import requests
from bs4 import BeautifulSoup

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
    # title = title.text.replace('\n', '')
    # price = price.text.replace('\n', '')
    # addr = addr.text.replace('\n', '')
    title = title.replace('\n', '')
    price = price.replace('\n', '')
    addr = addr.replace('\n', '')
    print(f'{title}, {price}, {addr}')
    f.write(f'{title}, {price}, {addr}\n')

f.close()

'''
<a class="card-link " data-event-label="618474119" href="/articles/618474119">
    <div class="card-photo ">
        <img alt="먹태깡 60봉" src="https://dnvefa72aowie.cloudfront.net/origin/article/202307/6c8195773a07c1b2eef20bc13beeb67201a847f86b69044ace35dc9e2d603739.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
    </div>
    <div class="card-desc">
      <h2 class="card-title">먹태깡 60봉</h2>
      <div class="card-price ">
        1,500원
      </div>
      <div class="card-region-name">
        경기도 김포시 장기동
      </div>
      <div class="card-counts">
          <span>
            관심 19
          </span>
        ∙
        <span>
            채팅 30
          </span>
      </div>
    </div>
</a>
'''
