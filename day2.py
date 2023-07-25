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

def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2

def square(number: int | float) -> int | float:
    return number ** 2
