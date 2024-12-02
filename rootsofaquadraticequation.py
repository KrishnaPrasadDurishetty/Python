import math
a = int(input('Enter a value = '))
b = int(input('Enter b value = '))
c = int(input('Enter c value = '))

r1 = (-b + math.sqrt(b**2 - 4 * a *c))/(2 * a)
r2 = (-b - math.sqrt(b**2 - 4 * a *c))/(2 * a)

print('The roots of quaderatic equation are = ',r1,r2)