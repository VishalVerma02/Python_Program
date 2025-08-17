#find max value of list without useing max  
l1=[3,2,6,9,10,2,5,2]
"""max_value=l1[0]
for x in l1:
    if x>max_value:
     max_value=x
print(max_value)"""

l1.sort()
print(l1)
print(l1[-1])