# let's create a list and get the square of each elements using mapping
lis=[1,2,3,4,5,6,7,8,9]
def square(x):
    return x*x
result=map(square,lis)
#converting from map datatype to list
result=list(result)
print(result)


#let's do the same task using lambda function
#but finding cube
result=map(lambda x:x*x*x,lis)
result=list(result)
print(result)