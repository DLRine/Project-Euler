from Utilities import factors

a = 600851475143 # 600851475143
r = factors(a)
for i in range(len(r)-1,-1,-1):
    if len(factors(r[i])) == 1:
        print(r[i])
