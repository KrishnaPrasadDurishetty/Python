year = int(input('Enter year = '))

if year % 100 == 0:
    if year % 400 == 0:
        print('Leapyear')
    else:
        print('Not a leapyear')
elif year % 4 == 0:
    print('Leapyear')
else:
    print('Not a leapyear')