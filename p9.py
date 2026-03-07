for i in range(1000):
    for j in range(1000):
        for x in range(1000):
            if i+j+x == 1000 and i**2+j**2==x**2 and i<j<x:
                print(f'i : {i}\nj : {j}\nx : {x}\nijx : {i*j*x}')
