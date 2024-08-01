print('Start Calculator')
num = 0
print(f'num = {num}')

while True:
    inp = input('>>> ')
    try :
        if inp == '=':
            print(f'num = {num}')
            break
        elif inp[0] == '+':
            num += float(inp[1:])
        elif inp[0] == '-':
            num -= float(inp[1:])
        elif inp[0] == '*':
            num *= float(inp[1:])
        elif inp[0] == '%':
            num %= float(inp[1:])
        elif inp[:2] == '//':
            num //= float(inp[2:])
        elif inp[0] == '/':
            num /= float(inp[1:])
        else:
            print('Invalid input')
            break
    except :
        print("Error")