sq = 0
for i in range(101):
    sq += i**2

qs = 0
for i in range(101):
    qs += i
    print(i, sq)
qs **= 2
print(qs-sq)