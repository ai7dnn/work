from openpyxl import Workbook
from random import randint, uniform
from datetime import datetime, timedelta
from faker import Faker

# Faker 객체 생성
fake = Faker()

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 헤더 생성
headers = ['Date', 'Name', 'Prod_ID', 'Price', 'Quantity', 'Total']
ws.append(headers)

# 데이터 생성 및 입력
for _ in range(100):
    date = datetime(2023, randint(1, 12), randint(1, 28))
    name = fake.word() + ' ' + fake.word() + ' ' + fake.word()
    prod_id = f'Prod_{randint(1, 10)}'
    price = round(uniform(10, 1000), 2)
    quantity = randint(1, 10)
    total = round(price * quantity, 2)
    row_data = [date, name, prod_id, price, quantity, total]
    ws.append(row_data)

# 파일 저장
wb.save('전자제품_판매관리.xlsx')
