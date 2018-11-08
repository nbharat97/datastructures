a= [39,9,45,63,18,81,108,54,72,36]
n = len(a)
for i in range(1,n):
    t = a[i]
    j = i -1
    while (t <= a[j] and j >= 0): 
        a[j+1] = a[j]
        j = j - 1
        print(i)
    a[j + 1] = t
    print(a)

print(a)
