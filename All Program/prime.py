# write a program to check whether a give number prime number or not
n=int(input("enter a number"))
i=2
while i<=n-1:
    if n%i==0:
        break
    i+=1
if i==n:
    print("prime number")
else:
    print("not prime nmber")