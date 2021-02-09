arr=[10,23,56,12,13,16]
for i in range(0,len(arr)):
    for j in range(len(arr)):
        if (arr[i]<=arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)