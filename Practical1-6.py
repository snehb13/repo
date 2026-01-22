n=int(input("enter no of elements : "))
arr=[]
x=[]
print("Enter elements :")
for i in range (n):
    ele=input()
    arr.append(ele)
print("Choose Rotation :")
print("1.Right")
print("2.Left")
choice=int(input("Enetr choice : "))

if(choice==1):
    x.append(arr[len(arr)-1])
    x.extend(arr[0:len(arr)-1])
if(choice==2):
    x.extend(arr[1:len(arr)])
    x.append(arr[0])
print(x)