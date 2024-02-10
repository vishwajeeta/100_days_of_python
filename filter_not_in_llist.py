list1=[8,5,6,4,9,3]
list2=[3,2,1]
result=filter(lambda a:a not in list1,list2)
print(f"items of list2 which are not in list1 are:\t{ list(result)}")