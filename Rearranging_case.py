str1 = input('Enter string = ')
lower = ''
upper = ''
for x in str1:
    if x.islower():
        lower += x
    else:
        upper += x
    str2 = lower + upper
print(str2)
