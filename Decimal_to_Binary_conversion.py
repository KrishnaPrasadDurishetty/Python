#decimal to binary conversion
#Here take input as string
n = int(input('Enter number to convert = '))
bin = '' #Take bin as empty string because it can save a considerable amount of space
while n > 0:
    r = n % 2
    bin = str(r) + bin
    n = n // 2
print(bin)