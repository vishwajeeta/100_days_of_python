#python filter takes two arguments
#it returns the value if it's true it won't if it's false
# let's create a list and get the elements which are lower than or equals 5 using filter method
lis=[1,2,3,4,5,6,7,8,9]
def condition(x):
    return x<=5

filt=filter(condition,lis)
print(type(filt))
#converting filter datatype to list
filt=list(filt)
print(filt)


#let's do the same thing using lambda function
filt=filter(lambda x:x>=5,lis)
print(list(filt))