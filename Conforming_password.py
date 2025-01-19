pass1 = input('Enter password = ')
pass2 = input('Conform password = ')

if pass1 == pass2:
    print('Yes, They are matching')
else:
    if pass1.casefold() == pass2.casefold():
        print('Check the cases and try again')
    else:
        print('No, They are not matching..Try again')