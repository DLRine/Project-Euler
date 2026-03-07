from math import sqrt
def factors(a):
    sq = sqrt(a)
    r = []
    for i in range(1, int(sq) + 1):
        if a % i == 0:
            r.append(i)
    return r

def allFactors(a):
    r = []
    for i in range(1,a+1):
        if a%i==0:
            r.append(i)
    return r

def isPalyndrom(elt):
    r = True
    elt = str(elt)
    for i in range(len(elt)//2):
        if elt[i] != elt[-i-1]:
            r = False
    return r