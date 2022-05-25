#Area Circle, Rectangle, Square, Triangle and Trapezium

def area(selectedType):
    if selectedType == 'Circle':
        radius = int(input("Please Enter the Radius: "))
        print("Area of the Circle is", str(3.1416*radius*radius))
    elif selectedType == "Triangle":
        height= int(input("Please Enter the height of the Triangle: "))
        base= int(input("Please Enter the base of the Triangle: "))
        print("Area of the Triangle is", str((height*base)/2))
    else:
        print("Please Enter either Circle or Triangle")
print("Possible area calulation: Circle, Triangle")
area(input("Please Enter your prefered Type: "))
