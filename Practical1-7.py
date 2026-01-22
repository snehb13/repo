n=int(input("enter no of elements : "))
arr=[]
x=[]
print("Enter elements :")
for i in range (n):
    ele=input()
    arr.append(ele)
m=int(input("Enter index to slice : "))
x.extend(arr[0:m])
for i in range(m):
    arr.pop(0)
print("Sliced Array : ",arr,"\t",x)
arr.extend(x)
print("Merged Array : ",arr)