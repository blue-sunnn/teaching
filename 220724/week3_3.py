inp = input("Enter 3 Mans : ")
a, b, c = inp.split('/')

a = int(a)
b = int(b)
c = int(c)

if a >= 25 or a % 3 != 0:
    print("A เป็นคนจริง")
    aa = True
else:
    print("A เป็นคนไม่จริง")
    aa = False

if b >= 25 or b % 3 != 0:
    print("B เป็นคนจริง")
    bb = True
else:
    print("B เป็นคนไม่จริง")
    bb = False

if c >= 25 or c % 3 != 0:
    print("C เป็นคนจริง")
    cc = True
else:
    print("C เป็นคนไม่จริง")
    cc = False

if aa or bb or cc:
    print("แก๊งคนจริง")
else:
    print("แก๊งคนไม่จริง")
