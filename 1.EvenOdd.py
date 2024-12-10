#This is a program to find a number is even or odd
def CheckEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input('Enter number = '))
print(CheckEven(n))
