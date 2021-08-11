# initializing lists 

test_list1 = []

for i in range(5) :
    print("Please Enter 5 Values For List 1 : ")
    test_list1.append(int(input()))

test_list2 = []

for i in range(5) :
    print("Please Enter 5 Values For List 1 : ")
    test_list1.append(int(input()))
  
# printing lists
print ("The first list is : " + str(test_list1))
print ("The second list is : " + str(test_list2))
  
# sorting both the lists
test_list1.sort()
test_list2.sort()
  
# using == to check if 

if test_list1 == test_list2:
    print ("The lists are identical")
else :
    print ("The lists are not identical")