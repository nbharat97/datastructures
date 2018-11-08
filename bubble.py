a = [1,2,3,4,5,6,30,54,7]

n = len(a)
flag = 0
for i in range(0,n-1):
    for j in range(0,n-1):

        if(a[j] > a[j+1]):
            flag = 1 #if the array is sorted then we do optimization

            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
    if flag == 0:
        print("Array is sorted")
        break 

print ("sorted array using bubble sort:")

print("\n")

print(a)
