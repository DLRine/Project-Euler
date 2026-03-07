fib = {1:1, 2:1}
def fibDyn(n:int):
    if n not in fib:
        fib[n] = fibDyn(n-1)+fibDyn(n-2)
    return fib[n]

r = 0
i = 2
a = fibDyn(1)
while a < 4000000:
    if a%2 == 0:
        r += a
    a = fibDyn(i)
    i += 1
print(r)