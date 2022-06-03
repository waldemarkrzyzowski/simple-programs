# program cheks numbers from 2 to 100
for candidate in range(2,100):
    # loop for executes from range 2 to variable candidate
    for divider in range(2,candidate):
        # if variable candiate has more divider - break
        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate,divider))
            break
    else:
            print("%2d is prime!" % (candidate))
            
        



