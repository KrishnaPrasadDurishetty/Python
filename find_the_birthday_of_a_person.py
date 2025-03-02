birthdays = {'sachin':'03/04/2003',
             'carl':'01/04/2001',
             'khan':'12/10/2006',
             'Donald':'06/14/2010',
             'Rohan':'01/06/2005'}
name = input('Enter name : ')
if name in birthdays:
    print('Mr/Miss {} was born on {}'.format(name, birthdays[name]))
else:
    print('Name not found')