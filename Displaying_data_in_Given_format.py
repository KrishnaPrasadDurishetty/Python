item = input('Enter item name = ')
price = input('Enter price = ')

total_length = len(item) + len(price)
dot = '.'*(25 - total_length)

print(item + dot + price)