def absolute(num):
    try:
        a = int(num)
        b = float(num)
        
        if num[0] == "-":
            return num[1:]
        else:
            return num
    
    except:
        return "Not valid input !!!"

print(absolute("-123"))