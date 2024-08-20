inp = input()

a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

empty = ""

if a % 2 == 0:
    empty += "even"
else:
    empty += "odd"

empty += " "

if b % 2 == 0:
    empty += "even"
else:
    empty += "odd"

empty += " "

if c % 2 == 0:
    empty += "even"
else:
    empty += "odd"

print(empty)