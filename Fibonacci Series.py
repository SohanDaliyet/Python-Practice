number_1 = int(input('Please give the first number :'))
number_2 = int(input('Please give the second number :'))
number_of_terms = int(input('Please give the number of terms :'))
a = number_1
b = number_2
count = 0
if number_of_terms <= 0:
    print('Invalid Input !!!')
elif number_of_terms == 1:
    print(b)
else:  
   print("Fibonacci sequence:")  
   while count < number_of_terms :  
       c = a + b  
       print(a)    
       a = b  
       b = c  
       count += 1  
