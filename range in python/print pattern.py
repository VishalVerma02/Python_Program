''' generate pattern like:1
                          12
                          123
                          1234
                          12345 using nested range loops.'''
for e in range(1,6,1):
    for i in range(1, e+1):
        print(i,end=' ')
    print() # move the next line after each row.
                          