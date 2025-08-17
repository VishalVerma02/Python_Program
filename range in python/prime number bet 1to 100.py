# print all prime number between 1 to 100 using range.
for e in range(2,101):
    is_prime=True
    for i in range(2, int(e**0.5) +1):
        if e%i==0:
            is_prime=False
            break
    if is_prime:
     print(e,end=' ')