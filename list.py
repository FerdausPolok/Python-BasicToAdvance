"""List is like other laguages Array but more Felxible"""

list1 = [0, 1, 2, 3, 4, 5, 6]
list2= ['a','b','c']
list3= [1,'a',2,3,7,'c']
print(list1)
print(list2)
print(list3)

print(list3[3])

#Nestead list

nstList1 = [[1,2,3,4],['A','B','C']]
print(nstList1)
print(nstList1[1])
print(nstList1[1][2])

#negetive Index

list4=[5,4,3,2,1]
print(list4[-1])

#Sublist and slicing

print(list1[0:5]) #list[start_index: end_index+1]
print(list1[:4])
print(list1[0:])
print(list1[:])

#Modifying list

list6=[1, 2, 3, 4]
list7=['x', 'y', 'z']

list67= list6 + list7
print(list67)

list8 = [1,2,3]
list9 = list8*3
print(list9)

#deleting element

list10=[1,2,3]
del list10[0]
print(list10)