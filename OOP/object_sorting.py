class Toy:
    def __init__(self,  name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


def print_toy_objects(toy_list):
    for obj in toy_list:
        print(f"Toy: {obj.name}, Price: {obj.price}")

toy_1 = Toy("A", 1000)
toy_2 = Toy("Cycle", 500)
toy_3 = Toy("Helicopter", 3000)


toys = [toy_1, toy_2, toy_3]

#using the built in sort function
toys.sort(key= Toy.sort_priority, reverse=True)
print_toy_objects(toys)

print("\n\n")

#using the sorted function
sorted_toys= sorted(toys, key=Toy.sort_priority)
print_toy_objects(sorted_toys)

print("\n\n")

#lamda function basic
result = lambda x,y,z: z+y+z
print(result(1,2,3))

print("\n\n")

#Sort Using the lamda function (its like arrow function in js)
toys_2 = [toy_3, toy_1, toy_2]
toys.sort(key= lambda x: x.price)
print_toy_objects(toys_2)
print("\n\n")

#Sorted Using the lamda function (its like arrow function in js)
sorted_toys_2 = sorted(toys_2, key=lambda x: x.price)
print_toy_objects(sorted_toys_2)


