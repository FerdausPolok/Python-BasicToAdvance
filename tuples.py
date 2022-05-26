#Tuples are immutable version of list that means we can't edit update this

tup= (1,2,3, 'hello', 9.8)
print(tup)
print(type(tup))
print(tup[4])

#tup to list
newList = list(tup)
print(newList)
print(type(newList))

#list to tup
new_tup = tuple(newList)
print(new_tup)
print(type(new_tup))


