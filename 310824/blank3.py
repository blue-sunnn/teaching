print(' *** Display vowel in small *** ')
inp = input('Enter something : ')
temp = ''

for i in range(len(inp)):
    if inp[i] == 'A':
        temp += 'a'
    elif inp[i] == 'E':
        temp += 'e'
    elif inp[i] == 'I':
        temp += 'i'
    elif inp[i] == 'O':
        temp += 'o'
    elif inp[i] == 'U':
        temp += 'u'
    else:
        temp += inp[i]

print(temp)
print('===== End Program =====')
