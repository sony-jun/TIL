a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)
for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            print(i, j, k)
print(a*b*c)
