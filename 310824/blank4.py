print(' *** Alphabet Sequence (a-z) *** ')
inp = input()
char, step, lenght = inp.split()

step = int(step)
lenght = int(lenght)
x = ord(char)

if step < 0:
    print('Invalid input !!!')
    exit()

for i in range(lenght):
    if x > ord('z'):
        x -= 26

    if i < lenght - 1:
        print(chr(x), end='-')
    else:
        print(chr(x))

    x += step
print('===== End Program =====')
