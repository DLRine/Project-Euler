# Same as p18
l = []
with open("p67.txt", 'r') as f:
    for line in f.readlines():
        line = line
        l.append(line[:len(line)- 1].split(' '))
        a = line[-1]
l[-1][-1] = l[-1][-1] + a

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])

for i in range (len(l) -2, -1, -1):
    for j in range(len(l[i])):
        l[i][j] += max(l[i+1][j], l[i+1][j+1])
print(l[0][0])