i = 2520
boo = True
while boo:
    boo = False
    for j in [20,19,18,17,16,15,14,13,12,11]:
        if i%j != 0:
            boo = True
    i +=2520
print(i-2520)