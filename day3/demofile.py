# demofile.py
for i in range(10):
    url = 'https://www.credu.com/?page=' + str(i)
    print(url)

for x in range(1, 6):
    # print(x, '*', x, '=', str(x*x).rjust(3))
    # print(f'{x}*{x} = {x*x}')
    print(f'{x}*{x} = {x*x:>3}')

for x in range(1, 6):
    print(x, '*', x, '=', str(x*x).zfill(5))

import math
print(f'{10}')
print(f'{10:x}')
print(f'{10:b}')
print(f'{10:o}')
print(f'{100*3456:,}')
print(f'{math.pi:10.4f}')

# %%
f = open(r'demo.text', 'wt', encoding='utf-8')
f.write('첫번째\n두번째\n세번째\n')
f.close()

f = open(r'demo.text', 'rt', encoding='utf-8')
result = f.read()
f.close()
print(result)

f = open(r'demo.text', 'rt', encoding='utf-8')
result = f.readlines()
f.close()
print(result)

f = open(r'demo.text', 'rt', encoding='utf-8')
result = f.readline()
f.close()
print(result)

f = open(r'demo.text', 'rt', encoding='utf-8')
result = f.readline()
print(f.tell())
print(result)

# %%
print(r'C:\work\demo')
print('C:\work\demo')

# %%
f = open(r'demo.text', 'rt', encoding='utf-8')
result = f.read()
f.seek(0)

print(f.readline(), end='')
print(f.readline(), end='')

f.seek(0)
result = f.readlines()
print(result)

f.close()
print(result)