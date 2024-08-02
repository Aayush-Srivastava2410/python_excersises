from math import sqrt

a = int(input('Coefficient of x^2:'))
b = int(input('Coefficient of x:'))
c = int(input('Constant:'))

D = b**2-4*a*c
R1= (-b+sqrt(D))/(2*a)
R2= (-b-sqrt(D))/(2*a)

print(f'root 1:{R1}, root 2:{R2}')
