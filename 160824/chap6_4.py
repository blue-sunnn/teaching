inp = [int(e) for e in input().split()]
empty = []
empty1 = []

for idx, i in enumerate(inp):
    if i % 2 == 0:
        empty.append(idx)

print(empty)

for idx, j in enumerate(inp):
    if idx in empty:
        empty1.append(inp[empty[-(empty.index(idx) + 1)]])
    else:
        empty1.append(j)

print(empty1)
