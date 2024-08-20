inp = [int(e) for e in input().split()]

num = inp[0]
most = 0 

for i in inp:
    now = inp.count(i)
    if now > most :
        most = now
        num = i

print(num)
