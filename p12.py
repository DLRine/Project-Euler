from Utilities import allFactors # i = 4460

i = 5454
r = 32
while r < 500:
    a = 0
    for j in range(i+1):
        a+= j
    r = len(allFactors(a))
    print(a, i, r)
    i +=1

print(a)
