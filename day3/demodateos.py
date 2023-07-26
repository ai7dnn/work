# %%
from datetime import *

d1 = date(2023, 7, 20)
print(d1)
d2 = date.today()
print(d2)
d3 = timedelta(days=100) + d2
print(d3)
d4 = datetime.now()
print(d4)

# %%
import random

print(random.random())
print(random.choice(range(10)))
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(2, 5), 2))
print(random.sample(range(1, 30), 10))

# %%
from os.path import *
abspath('python.exe')
basename('c:\\python310\\python.exe')
getsize('c:\\python310\\python.exe')
if isfile('c:\\python310\\python.exe'):
    print('file exists')
else:
    print('file do not exists')


# %%
lotto = list(range(1, 46))
random.shuffle(lotto)
print(lotto)

# %%
from os import *

print(dir())
name
environ
system('notepad.exe')

getcwd()
chdir('..')
chdir('d:\hskang\work')

# %%
import glob
result = glob.glob('*.py')
print(result)

for item in glob.iglob('*.*'):
    print(item)
