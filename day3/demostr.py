# %%
print( dir(str) )

# %%
sA = '파이썬은 강력해'
sB = 'python is very powerful'

len(sA)
len(sA)
print(sB.capitalize())
print(sB.count('p'))
print(sB.count('p', 7))

print(sB.startswith('python'))
print(sB.endswith('ful'))
result = sB.upper()
print(result)
result = sB.lower()
print(result)

data = ' spam and ham '
result = data.strip()
print(data)
print(result)

data = '<<<  spam and ham >>>'
result = data.strip('><, ')
print(data)
print(result)

result2 = result.replace("spam", 'spam egg')
print(result)
lst = result2.split()
print(lst)

print(";)".join(lst))

data2 = "spam::ham::egg"
result3 = data2.split("::")
print(result3)

print('MBC2580'.isalnum())
print('MBC:2580'.isalnum())
print('2580'.isdigit())
print('2580'.isdecimal())

# %%
import re
# p = r'.'
p = r'[py]'

m = re.search(p, 'python')
print(m)
lst = re.findall(p, 'python')
print(lst)

import re
# p = r'.'
p = r'\w*'
s = 'py3879& $%^& python'
m = re.search(p, s)
print(m)
lst = re.findall(p, s)
print(lst)

# %%
