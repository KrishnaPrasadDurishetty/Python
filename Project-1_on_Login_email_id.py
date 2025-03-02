print('\t\t*SIGNUP PAGE*')
fn = input('Enter first name  : ')
ln = input('Enter last name   : ')
email = input('Enter email id    : ')
psw1 = input('Enter Password    : ')

if email.endswith('@gmail.com'):
    print('Valid Email ID')

    print('\t\t*LOGIN PAGE*')
    login_email = input('Enter email id    : ')

    if email == login_email:
        print('Valid Email ID')
        login_psw = input('Enter Password    : ')
        if psw1 == login_psw:
            print('Login successfull')
        else:
            print('Wrong Password!...')
            print('Login Failed')
    else:
        print('Wrong Eamil ID')
        print('Login Failed')
else:
    print('Incorrect email id')
    print('Login Failed')