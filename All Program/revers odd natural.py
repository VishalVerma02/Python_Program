# write a python script to print first 10 odd natural number in revers
n=int(input("enter a number"))
i=10
if n%2!=0:
    while i>0:
        print(n)
        n-=2
        i-=1
else:
    n-=1
    while i>0:
        print(n)
        n-=2
        i-=1        
        
