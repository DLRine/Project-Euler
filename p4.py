from Utilities import isPalyndrom

r = []
for i in range(999, -1, -1):
    for j in range(999, -1, -1):
        a = i*j
        if isPalyndrom(a):
            r.append(a)
r.sort(reverse=True)
print(r[0])
print(r)