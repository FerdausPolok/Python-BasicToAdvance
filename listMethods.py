place_viisted= ['India', 'uk', 'Nepal', 'ak', 'Vutan', 'Austria', ]

#index method
print(place_viisted.index('Nepal'))

#append method-> Element add at last
place_viisted.append('Africa')
print(place_viisted)

#insert method -> Insert in list (whichIndex, whatElement)
place_viisted.insert(1, 'UK')
print(place_viisted)

#remove method -> Delete any avalue (value)
place_viisted.remove('Nepal')
print(place_viisted)

#sort /trim sorting algo used here
place_viisted.sort() #capital sort than small sort
print(place_viisted)

place_viisted.sort(key=str.lower) #lower alpha sort
print(place_viisted)

place_viisted.sort(key= str.lower, reverse=True) #higher alpha sort
print(place_viisted)
