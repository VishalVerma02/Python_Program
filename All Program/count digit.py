#write a python script to count digit a given number
n=int(input("enter a number"))
count=0
temp=abs(n)
if n==0:
    count=1
else:
    while temp>0:
        temp//=10
        count+=1
print(count)        
    