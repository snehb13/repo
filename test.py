def fact(i):
    f=1
    for j in range(1,i+1):
        f=f*j
    return f

for i in range(7):
    for j in range (i+1):
        print("*", end="")
    print("")    
    print("factorial ", i,"= ", fact(i))

