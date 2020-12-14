#This is the given question.

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

# Solution :

def makes_twenty(n1,n2):

    #return (n1+n2) == 20 or n1==20 or n2==20
#The above code is the Shorter and Efficient.You can use it as per your convenience.
#The below code will be relatively easier to undestand.They are one and the same thing.
    
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

n1 = int(input('Please Enter The First Number : '))
n2 = int(input('Please Enter The Second Number : '))

print(makes_twenty(n1,n2))
