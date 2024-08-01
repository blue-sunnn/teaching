inp = input("Enter Triangle size : ")

try :
    num = int(inp)
    if num < 3:
        print("เหลี่ยมไปนิสนึง")
        exit()

    while num > 0:
        print('*' * num)
        num -= 1

except ValueError:
    print("เหลี่ยมจัด")