"""
TEXT FILE->
1. 'r' (Read)
2. 'r+' (Read + Write)
3. 'w' (Writing)
4. 'w+' (writing + reading)
5. 'a' (appending) -Edit with the previous
6. 'a+' (Appending + reading)


#open a file
f = open('a.txt', 'w')
#getting some info from file
print("name= ",f.name)
print("Is it closed? ", f.closed)
print("Mode= ",f.mode)
#writting
f.write("Python is cool. ")
f.close()


#appending
f = open('a.txt', 'a')
#updating
f.write("Java is also cool")
f.close()



#Read +
f = open('a.txt', 'r+')

info = f.read(12)
print(info)
f.close()

"""
#Read and White
f = open('a.txt', 'w+')
f.write("All is lost")
f.close()







