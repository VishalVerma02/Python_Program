#write a python script to calculate sum of the digit of a given number
num=int(input("enter a number"))
result=0
temp=abs(num)

while temp>0:
    result+=temp%10
    temp//=10
print(result)