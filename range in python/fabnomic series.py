# print the fibonacci series up to 10 terms using range.
n=10
a,b=0,1
print("fibonacci series up to 10 terms")
for e in range(n):
    print(a, end=" ")
    a,b=b,a+b
    