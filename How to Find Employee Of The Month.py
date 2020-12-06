work_hours = [('Abby',100),('Billy',400),('katty',800)]
#These are predefined values in the terms of (Employee,Number of hours worked)

register = input('Do You Want To Register A New Employee ? [Y/N] :').capitalize().strip()

if register == 'Y' :
    
    employee = input('Please Enter The Name Of The Employee :').capitalize().strip()
    hours = int(input('Please Enter The Number Of Hours Worked :'))
    print('The Newly Registerd Employee Is ',employee,'And The Number Of Hours Worked Are ',hours)
    employee_hours = (employee,hours)

    work_hours.append(employee_hours)

else:
    pass

def employee_check(work_hours):

    current_max = 0
    employee_of_the_month = ''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return(employee_of_the_month,current_max)

check_winner = input('Do You Wish To Check The Current Employee Of The Month ? [Y/N] :').capitalize().strip()

if check_winner == 'Y' :
    
    print(employee_check(work_hours))

else:
    pass

