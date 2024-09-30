# from math import sqrt
# number=int(input("enter your number:"))
# if number>1:
#     for i in range(2,int(sqrt(number))+1):
#         if number%i==0:
#             print(number, "is not prime")
#             break
#     else:
#             print(number,"is prime")
# else:
#      print("not a prime number")
def primes(n):
    prime=[True for i in range(n+1) ]
    currentnumber=2
    while(currentnumber*currentnumber<=n):
        if(prime[currentnumber]==True):
            for i in range(currentnumber **2,n+1,currentnumber):
                prime[i]=False
        currentnumber+=1
    prime[0]=False
    prime[1]=False
    for p in range (n+1):
        if prime[p]:
            print(p)
n=int(input("enter number to find all prime numbers"))
primes(n)






                 