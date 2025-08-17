# Print all perfect squares between 1 and 500 using range().
for i in range(1,501):
    if i**0.5==int(i**0.5):
      print(i,end=" ")
    