def printPrimeNumbers(lower,upper):
    for i in range(lower,upper+1):
        flag=True
        for j in range(2,i):
            if(i%j==0):
                flag=False
                break
        if(flag):
            print(i)    

lower=int(input("Enter lower limit : "))
upper=int(input("Enter upper limit : "))
printPrimeNumbers(lower,upper)