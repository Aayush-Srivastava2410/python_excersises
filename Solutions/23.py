s = int(input('Enter Seconds:'))
m = s//60
h = m//60
m = m%60
s=s%60

print(f'{h}:{m}:{s}')