from Utilities import factors
i = 2
r = []
while len(r)<10001:
    if len(factors(i)) == 1:
        r.append(i)
    i += 1
print(r[-1])