a = int(input('Enter starting value = '))
d = int(input('Enter common difference = '))
n = int(input('Enter end value = '))

for f in range(a , a + n * d , d):
    print(f)