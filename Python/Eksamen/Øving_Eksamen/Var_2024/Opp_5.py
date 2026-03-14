n = 10
a = [0, 1]

for i in range(2, n+1):
    a.append(a[i-1] + a[i-2])
    if a[i] % 2 == 0:
        print(a[i])
print(a[n])