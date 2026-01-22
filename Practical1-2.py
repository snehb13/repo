n=int(input("enter Number : "))
a,b=0,1
print("Fibonacci Series :")
for i in range(n):
    print(a,"\t")
    c=a+b
    a=b
    b=c