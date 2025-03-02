l = [10,20,30,40,50]
try:
    index = int(input('Enter a index '))
    print(l[index])
    print('end of try block')
    '''except IndexError:
        print('Invalid Index')
    except ValueError:
        print('Enter only integer value')
    except:
        print('Some Error')'''
except (IndexError , ValueError) as msg:
    print(msg)
print('Termianated Gracefully')