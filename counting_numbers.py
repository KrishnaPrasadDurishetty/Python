n = int(input('Enter number = '))
counter = 0
while n > 0:
    n = n // 10
    counter = counter + 1
print(counter)