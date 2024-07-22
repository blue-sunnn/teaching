print(" *** Transform second *** ")

time = input("Enter seconds : ")

try:
    t = int(time)
    print(f"{t:,} seconds ==> ", end='')
    
    if t >= 604800: # weeks
        w = t // 604800
        print(w, "weeks", end='')

    if t >= 86400: # days
        d1 = t % 604800 // 86400
        d2 = t // 86400
        if t > 604800 and d1 > 0:
            print(d1, "days", end='')
        elif t < 604800:
            print(d2, "days", end='')

    if t >= 3600: # hours
        h1 = t % 86400 // 3600
        h2 = t // 3600
        if t > 86400 and h1 > 0:
            print(h1, "hours", end='')
        elif t < 86400:
            print(h2, "hours", end='')

    if t >= 60: # minutes
        m1 = t % 3600 // 60
        m2 = t // 60
        if t > 3600 and m1 > 0:
            print(m1, "minutes", end='')
        elif t < 3600:
            print(m2, "minutes", end='')
            
    if t >= 0: # seconds
        s1 = t % 60
        if t > 60 and s1 > 0:
            print(s1, "seconds", end='')
        elif t < 60:
            print(t, "seconds", end='')

except ValueError:
    print(f"! ! ! please enter a whole nunmber ==> {time}")

print(" ")
print(" --- program end --- ")
