#write a python script to calculate sum of first N natural number
n=int(input("enter a number"))
i=1
s=0
while i<=n:
    s=s+i
    i+=1
print("sum is ",s)