n = int(input('Enter number = '))
num = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
if num == rev:
    print('Palindrome')
else:
    print('Not a palindrome')