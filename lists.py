# we can store numbers in the list 
list1=[1,2,3,4,5,6,7,8]
print(list1)
print(type(list1)) #printing data type of the list
#getting the length of the list
print(f"Length of the list is:{len(list1)}")
# adding value
list1.append(77)
print(list1)
# getting the index value of the list item
print(f"index value of {77} is:{list1.index(77)}")
# inserting the value in the assigined indexed 
list1.insert(9,44) #first argument is index value and the second one is value to be inserted on that particular index
print(list1)

#removing list
list1.remove(77) #number 77 will be removed form the list
print(list1)

# appending two lists or adding two lists
list2=[10,20,30,40,50]
# list1.append(list2)
#       or 
list1+=list2
print(list1)

#changing the datatype of the list to tuple
print(f"Before changing the value:\t{type(list1)}")
list1=tuple(list1)
print(f"After changing the value:\t{type(list1)}")