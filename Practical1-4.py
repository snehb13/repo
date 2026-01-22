def isArmstrongNumber():
    ans=0
    for i in range(len(num)):
        ans+=int(num[i])**len(num)
    result=(False,True)[ans==int(num)]
    return result

num=input("Enter Number : ")
print("Choose way to check Armstrong Number :")
print("1.Without User defined function")
print("2.With User defined function")
choice=int(input("Enter your choice : "))
if(choice==1):
    ans=0
    for i in range(len(num)):
        ans+=int(num[i])**len(num)
    result=(False,True)[ans==int(num)]

if(choice==2):
    result=isArmstrongNumber()
    
if(result):
    print(int(num)," is an Armstrong Number")
else:
    print(int(num)," is not an Armstrong Number")