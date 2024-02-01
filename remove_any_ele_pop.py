list=[3,4,3,2,9,7]
print("before:",list)
index=3
if index < len(list)-1:
    list[len(list)-1]=list[index]
print("after operation:",list)
list.pop()
print("after poping:",list)