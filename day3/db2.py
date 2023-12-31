import sqlite3 

# 파일에 저장
con = sqlite3.connect("D:\\hskang\\work\\sample.db")
# 메모리에 저장
# con = sqlite3.connect(":memory:")

# 커서 객체
cur = con.cursor()

# 테이블 구조 생성
cur.execute('create table if not exists PhoneBook ' +
    '(id integer primary key autoincrement, ' +
    'name text, phoneNum text);')

# 1건 입력
cur.execute('insert into PhoneBook (name, phoneNum) values ' +
    '("홍길동", "010-111");')

# 입력 패러미터 처리
name = '전우치'
phoneNumber = '010-222'
cur.execute('insert into PhoneBook (name, phoneNum) values ' +
    '(?, ?);', (name, phoneNumber))

# 다중 행을 입력, 둘다 가능
# datalist = (('이순신', '010-333'), ('박문수', '010-123'))
datalist = [('이순신', '010-333'), ('박문수', '010-123')]
cur.executemany('insert into PhoneBook (name, phoneNum) values ' +
    '(?, ?);', datalist)

# 커밋
con.commit()

# 검색 구문
cur.execute('select * from PhoneBook;')
print(cur.fetchall())
# for row in cur:
#     print(row)

# %% 조회만
import sqlite3 

# 파일에 저장
con = sqlite3.connect("D:\\hskang\\work\\sample.db")
# 커서 객체
cur = con.cursor()

# 검색 구문
cur.execute('select * from PhoneBook;')
print(cur.fetchall())
