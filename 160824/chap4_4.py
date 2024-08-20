def slope(a, b, c):
    try:
        return str(int(-a/b))
    except:
        return "Not Available"
    
def xIntercept(a, b, c):
    try:
        return str(int(-c/a))
    except:
        return "Not Available"

def yIntercept(a, b, c):
    try:
        return str(int(-c/b))
    except:
        return "Not Available"

print()
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
print("Slope = " + slope(a, b, c))
print("x-intercept => " + xIntercept(a, b, c))
print("y-intercept => " + yIntercept(a, b, c))
