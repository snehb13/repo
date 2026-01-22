n=int(input("enter no of elements : "))
arr=[]
flag=True
print("Enter elements :")
for i in range (n):
    ele=int(input())
    arr.append(ele)
if(arr[0]<arr[1]):
    for j in range(1,n-1):
        if(arr[j]>arr[j+1]):
            flag=False

if(arr[0]>arr[1]):
    for j in range(1,n-1):
        if(arr[j]<arr[j+1]):
            flag=False

if(flag):
    print("The array is Monotonic")
else:
    print("The array is not Monotonic")