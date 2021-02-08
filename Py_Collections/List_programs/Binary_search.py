arr = [11, 10, 12, 19, 14, 15, 18, 20, 16, 13, 17]
elem = int(input("Enter the element to be found:"))
arr.sort()
flg=0
low=0
up=len(arr)-1
while(low<=up):
    mid=(up+low)//2
    if(elem>arr[mid]):
        low=mid+1
    elif(elem<arr[mid]):
        up=mid-1
    elif(elem==arr[mid]):
        flg=1
        break
if(flg==0):
    print("element not found")
else:
    print("element found")

