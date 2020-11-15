number = int(input('Please enter a digit :'))
def decimal_to_binary(number):
    if number > 1:
        decimal_to_binary(number // 2)
    print(number % 2,end = '')
decimal_to_binary(number)
