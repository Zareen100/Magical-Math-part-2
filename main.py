from math import sqrt
number=int(input("enter your number:"))
if number>1:
    for i in range(2,int(sqrt(number))+1):
        if number%i==0:
            print(number, "is not prime")
            break
    else:
            print(number,"is prime")
else:
     print("not a prime number")




                 