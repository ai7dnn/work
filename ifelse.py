# ifelse.py
# score = int(input('점수 입력: '))

# if 90 <= score:
#     grade = 'A'
# elif 80 <= score:
#     grade = 'B'
# elif 70 <= score:
#     grade = 'C'
# else:
#     grade = 'D'

# print('grade:', grade)

# %%
value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, '문자열', 3.14]
for i in lst:
    print(i)
    
# %%
print('== break ==')

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lst:
    if i%2 == 0:
        continue
    # print(f'item:{i}')
    print('item:{}'.format(i))

# %%
print(list(range(10)))
print(list(range(1, 100, 10)))
print(list(range(1, 32)))

# %%
