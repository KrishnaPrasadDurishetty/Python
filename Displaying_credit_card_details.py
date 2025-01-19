cardno = input('Enter card Number = ')
if len(cardno) == 19:
    last_digits = cardno[15::]
    four = '*' * 4 + ' '
    print(four * 3 + last_digits)
else:
    last_digits = cardno[12::]
    four = '*' * 4 + ' '
    print(four * 3 + last_digits)