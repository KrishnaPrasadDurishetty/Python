num_of_nums = int(input('Enter number of numbers = '))
count = 0
max = 0
while count < num_of_nums:
    n = int(input('Enter number = '))
    if n >= max:
        max = n
    count += 1
print('Max number is = ',max)