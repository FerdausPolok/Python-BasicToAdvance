#inheritance means inheriting other classes property method into my class
class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f"{self.name} is moving forward")
    def move_backward(self):
        print(f"{self.name} is moving backward")
    def move_left(self):
        print(f"{self.name} is moving left")
    def move_right(self):
        print(f"{self.name} is moving right")

class HouseBot(Robot): #Houbot Inherits Robot
    def __init__(self, name, version, area_covered):
        super().__init__(name, version) #super class er constructor ei class a age dewa
        self.area_covered = area_covered #erpor amader extra ta

    #our aditional methor

    def clean(self):
        if self.area_covered>0:
            print(f"{self.name} is cleaning the house")
            self.area_covered -=30

            if self.area_covered<0:
                self.area_covered=0
        else:
            print("All Cleaned. Please reset the area covered perameter")

    def set_cover_area(self, area):
        if self.area_covered == 0:
            self.area_covered= area
        else:
            print("I CAN STILL CLEAN MORE")

    @staticmethod
    def stop():
        print("I had been stoped")

    #Method overryding
    def move_forward(self):
        print("This is in houbot class, overridden function")
        super().move_forward()




hBot = HouseBot("Polok", 1.1, 50)
print(hBot.name)
print(f"Total covered area = {hBot.area_covered} sqr inches")
hBot.move_forward()

print("\n\n")

hBot.clean()
hBot.clean()
hBot.clean()

hBot.set_cover_area(10)

hBot.clean()
hBot.clean()

print("\n\n")

hBot.move_forward()

print("\n\n")

robo = Robot("Zaman", 1.2)
print(help(Robot))
print(help(HouseBot))

print("\n\n")

print(issubclass(HouseBot, Robot))
print(issubclass(Robot, HouseBot))
print(issubclass(Robot, object))
print(issubclass(HouseBot, object))

print("\n\n")

print(isinstance(hBot, Robot))
print(isinstance(hBot, HouseBot))
print(isinstance(hBot, object))
print(isinstance(robo, object))







#which class we inherit - > Super class / Mother class
#that class which is inheriting -> child class/ sub class

