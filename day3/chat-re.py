import re

# 주민번호에 맞는 정규식 패턴
pattern = r'^\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])-[1-2]\d{6}$'

def validate_jumin(jumin):
    # 주민번호가 정규식 패턴과 일치하는지 확인
    if re.match(pattern, jumin):
        return True
    return False

# 테스트할 주민번호 예시
valid_jumin = '950101-1234567'
invalid_jumin = '990215-1234567'

# 주민번호 유효성 검사
print(validate_jumin(valid_jumin))    # True
print(validate_jumin(invalid_jumin))  # False

import re

# 주민번호에 맞는 정규식 패턴
pattern = r'^\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])-[1-2]\d{6}$'

# 정규식에 맞는 문자열 5개
valid_jumin_list = [
    '950101-1234567',
    '990215-1234567',
    '031231-2345678',
    '070606-3456789',
    '880707-4567890'
]

# 정규식에 맞지 않는 문자열 5개
invalid_jumin_list = [
    '123456-1234567',
    '990215-123456',   # 6자리가 아닌 경우
    '021531-2345678',  # 존재하지 않는 날짜
    '990101-12345678', # 13자리가 아닌 경우
    '070606#3456789',  # '-' 대신 다른 문자로 구분
    '070606+3456789',  # '-'이 아닌 다른 문자로 구분
]

def validate_jumin(jumin):
    # 주민번호가 정규식 패턴과 일치하는지 확인
    if re.match(pattern, jumin):
        return True
    return False

# 정규식에 맞는 문자열 출력
print("정규식에 맞는 문자열:")
for jumin in valid_jumin_list:
    print(f"{jumin}: {validate_jumin(jumin)}")

# 정규식에 맞지 않는 문자열 출력
print("\n정규식에 맞지 않는 문자열:")
for jumin in invalid_jumin_list:
    print(f"{jumin}: {validate_jumin(jumin)}")
