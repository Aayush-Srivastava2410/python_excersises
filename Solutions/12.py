x = int(input('Enter a number:'))
if x%7 == 0:
    if x%2 == 0:
        print('It is an even multiple of 7')
    else:
        print('It is an odd multiple of 7')
else:
    print('It not an multiple of 7')