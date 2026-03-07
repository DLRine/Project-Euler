from Utilities import factors
r = 0
for i in range(2,2000000):
    if len(factors(i)) == 1:
        r += i
    print(i)
print(r)