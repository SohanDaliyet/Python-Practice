# This is the code for Future Value

# F = ( 1 + i )^t

#The terms of the formula are :
#   F - Future value of account after given time period
#   P - Present value of account
#   i - Monthly interest
#   t - Number of months

# Now requesting details from client side.

def Request_For_Details() :
    present_value = float(input('Please enter the present value :'))
    monthly_interest_rate = float(input('Please enter the monthly interest rate :'))
    monthly_interest_rate /= 100
    number_of_months = int(input('Please enter the number of months the money will be left in the Account :'))

    return present_value, monthly_interest_rate, number_of_months

# Now Calculating Future Value

def Future_value( present_value, monthly_interest_rate, number_of_months) :
    future_value = present_value * ( 1 + monthly_interest_rate ) ** number_of_months

    return future_value

# Now main function

def main() :
    present_value, monthly_interest_rate, number_of_months = Request_For_Details()
    print("An Account with present value ", present_value, " at a ", monthly_interest_rate, " monthly interest rate left in the account for ", number_of_months, " months will yeild you you a future of ", Future_value( present_value, monthly_interest_rate, number_of_months))

main()    