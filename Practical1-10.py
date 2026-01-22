n=int(input("enter no of elements : "))
arr=[]
x=[]
print("Enter elements :")
for i in range (n):
    ele=int(input())
    arr.append(ele)
x=arr.copy()
x.sort(reverse=True)
m=int(input("No of Maximum elements to display : "))
if(m<=n):
    print(x[0:m])
else:
    print("these many numbers doesn't exist in the array.")