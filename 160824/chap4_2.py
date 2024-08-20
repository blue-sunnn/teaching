def quadraticChecker(a :float, b :float, c :float):
    underroot = b**2 - 4 * (a * c)

    if underroot < 0:       return 0
    elif underroot == 0:    return 1
    else:                   return 2

print()
print()
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

checker = quadraticChecker(a, b, c)
if checker == 0:
    print("No VALID")
elif checker == 1:
    print("ONE")
else:
    print("TWO")