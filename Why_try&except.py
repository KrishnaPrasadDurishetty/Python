def div(a, b):
    if (b != 0):
        c = a // b
        return c
    else:
        return -1
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))

'''c = div(a, b)
if c == -1:
    print('Division By zero')
else:
    print(c)'''

try:
    c = a // b
    print(c)
except:
    print('Zero Division Error')