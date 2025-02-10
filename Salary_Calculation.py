worked_hours = [int(x) for x in input('Enter hours per day in entire week,separated by spaces = ').split()]
wages = int(input('Enter hourly wages = '))
total = sum(worked_hours)
salary = total * wages
print('Salary = ',salary)