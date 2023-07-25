# %%
def times(a, b):
    return a*b

times
times(4, 5)

# %%
def times(a, b) -> int:
    return a*b

times
times(4, 5)

# %%
def connectURL(server, port):
    strURL = 'https://' + server + ":" + port
    return strURL

print(connectURL('naver.com', '80'))
print(connectURL(port='8080', server='daum.net'))

# %%
g = lambda x, y: x*y
g(2, 3)

# %%
data = 100

# %%
# type hints

# def square(number: union[int, float]) -> union[int, float]:
#     return number ** 2

def square(number: int | float) -> int | float:
    return number ** 2

# %%
# str = 'data'
class GString:
    def __init__(self):
        self.str = ''
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)

g = GString()
g.set('First Message')
g.print()
# %%
p = object()
