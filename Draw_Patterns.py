'''for i in range(0 , 5):
    for j in range(0 , 5):
        print('*', end = ' ')
    print('')'''
                    #(or)
'''for i in range(0 , 5):
    print('# '*9)'''


                    #(or)
'''for i in range(0 , 5):
    print('* '*(i + 1))'''
                    #(or)
for i in range(0 , 5):
    for j in range(0 , 5):
        if i >= j:
            print('*', end = ' ')
    print('')