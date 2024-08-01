inp = input("Enter Num : ")
num = int(inp)
if num < 1:
    print("Invalid Input")
    exit()
i = 1
sum = 0
mul = 1
while (i <= num):
    if i != num:
        print(f"{i}", end=",")
    else:
        print(f"{i}", end="\n")
    mul = mul * i
    sum = sum + i
    i = i + 1
print(f"Sigma(1 to {num}) = {sum}")
print(f"Factorial({num}) = {mul}")
