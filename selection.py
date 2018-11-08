a = [39,9,81,45,90,27,72,18]

n = len(a)
for i in range(0,n-1):

    s = a[i]
    for j in range(i+1,n):
        if (s >= a[j]):
            s = a[j]
            t = a[i]
            a[i] = a[j]
            a[j] = t
    print(a) # This is actually to check the iterations that is performed
print(a)
