work_hours = [('Abby',100),('Billy',400),('katty',800)]
#These are predefined values in the terms of (Employee,Number of hours worked)
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

