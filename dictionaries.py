#it is a ds that have it's own id/index/key (any type) and can store value agaist that

dict1 ={}
print(type(dict1))

my_stuff= {
    'book': ['Misir Ali', 'Himu'],
    'phone': 'Samsung',
    'home': 'BD'
}

print(my_stuff)
print(my_stuff['book'][0])
print(my_stuff['book'][1])
print(my_stuff['home'])

a= [100, 200]
b= [200, 100]
print("List check:",a==b)

c= {1: 100, 2: 200}
d= {2: 200, 1: 100}
print("Dict check:",c==d)

#connecting two dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'c': 300, 'd': 400}

d3= d1.copy()
d3.update(d2)

print(d3)



