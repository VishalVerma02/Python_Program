# write a python script to check whether a given number is a three digit number or not
x=int(input("enter a digit"))
if x>=100 and x<=999 or x<=-100 and x>=-999:
    print("this is three digit number")
else:
    print("this is not three digit number")