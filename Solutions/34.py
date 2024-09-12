n = int(input('Enter a number:'))
og = n
s=0
while(n>0):
    digit=n%10
    s=s+(digit**3)
    n=n//10

if s==og:
    print('Armstrong number')
else: print('Not an Armstrong number')