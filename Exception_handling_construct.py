l = [10,20,30,40,50]
try:
    index = int(input('Enter a index '))
    print(l[index])
    print('end of try block')
except:
    print('Invalid Index')
print('Termianated Gracefully')