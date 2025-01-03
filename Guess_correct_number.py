import random
n = random.randint(1,10)
guess = 0
while guess != n:
    guess = int(input('Enter your guess = '))
    if guess < n:
        print('It is lesser')
    elif guess > n:
        print('It is greater')
    else:
        print('Yes,Your guess is correct')