import re
# p = r'.'

p = r'\w*'
s = 'py3879& $%^& python'
m = re.search(p, s)
print(m)
lst = re.findall(p, s)
print(lst)


# %% 
import re
p = '[0-9]*th'
s = '35th'

r = re.search(p, s)
print(r)
print(r.group())

p = '[0-9]*th'
s = '35th'

r = re.match(p, s)
print(r)
print(r.group())

p = 'apple'
s = '빅테그에서 apple의 위상'
r = re.search(p, s)
print(r)
print(r.group())

p = '\d{4}'
s = '올해는 2024년'
r = re.search(p, s)
print(r)
print(r.group())

p = '\d{5}'
s = '우리 동네는 42300'
r = re.search(p, s)
print(r)
print(r.group())

# %% 대소문자
p = 'apple'
s = 'Apple is big company and apple is very delicious'
c = re.compile(p, re.IGNORECASE)
print(c.findall(s))

p = 'apple'
s = '''파이썬을
배워서

누구나 사용'''
p = '^.+'
c = re.compile(p, re.MULTILINE)
print(c.findall(s))

c = re.compile(p)
print(c.findall(s))

# %%
import re

def extract_emails(text):
    # 이메일 주소를 찾는 정규식 패턴
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # 정규식 패턴과 일치하는 모든 문자열 찾기
    emails = re.findall(pattern, text)

    return emails

# 테스트할 문자열
text = "이것은 테스트 문장입니다. example@example.com과 contact@domain.co.kr은 유효한 이메일 주소입니다. 그러나 abc@def과 abcd.com은 올바른 형식이 아닙니다."

# 정규식을 사용하여 이메일 주소 추출
extracted_emails = extract_emails(text)

# 추출된 이메일 주소 출력
print(extracted_emails)