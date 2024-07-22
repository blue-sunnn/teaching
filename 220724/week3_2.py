inp = input("Enter Number / Number : ")
num1, num2 = inp.split()

num1 = float(num1)
num2 = float(num2)

try:
    ans = num1 / num2
    print("------------------------------------------")
    print(f"| เก่งมากพี่ {ans:>30} |")
    print("------------------------------------------")
except:
    print("------------------------------------------")
    print("| พี่หารศูนย์ไม่ได้ ! ! !                 bruh |")
    print("------------------------------------------")
