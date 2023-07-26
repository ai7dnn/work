def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"            
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"

s = http_error(400)  
print(s)
s = http_error(404)  
print(s)
s = http_error(418)  
print(s)
s = http_error(500)  
print(s)

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
