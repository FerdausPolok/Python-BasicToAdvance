identity={
    'name': 'Polok',
    'age': 24,
    'occupation': 'Student'
}

#to print only the values
for i in identity.values():
    print(i)

#to print only the keys
for i in identity.keys():
    print(i)

#to print keys and values
for i in identity.items():
    print(i)

#a handy trick to print both under a loop
for k,v in identity.items():
    print(k,v)

#convert dict values and keys into a list

x= list(identity.keys())
y= list(identity.values())

print(x,y)

#in keyboard
print('name' in identity)
print('Polok' in identity)

#in keyboard - in values
print('name' in identity.values())
print('Polok' in identity.values())

#in keyboard - in keys
print('name' in identity.keys())
print('Polok' in identity.keys())

#the get() method
print(str(identity.get('name', 'not found')))
print(str(identity.get('height', 'not found')))

#the setdefault() Method
print(str(identity.setdefault('name', 'Ferdaus')))
print(str(identity.setdefault('height', '5ft 10in')))

print(identity)
