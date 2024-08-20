inp = [int(e) for e in input().split()]
odd = []
even = []

for i in inp:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd + even)
odd.reverse()
print(odd + even)
