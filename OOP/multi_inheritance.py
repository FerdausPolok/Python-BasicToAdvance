class Dancer:
    def __init__(self, style):
        self.style = style
    def dance(self):
        print(f"Dancing in {self.style} style")

class Singer:
    def __init__(self, genre):
        self.genre = genre
    def sing(self):
        print(f"The Singer is Singing {self.genre} Music")

class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material
    def painting(self):
        print(f"The painter is painting on {self.painting_material} material")

#Multiple Inheritance
class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genre, paint_material, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genre)
        Artist.__init__(self,paint_material)
        self.sport = sport
    def play_sport(self):
        print(f"Playing {self.sport}")

    #overriding the dance method od dancer class
    def dance(self, competition="Wprld championship"):
        print(f"Dancing with my own {self.style} style in the {competition} competition")

s = SuperHuman("Hip-Hop", "Classical", "Acrylic", "Football")

print(s.style)
print(s.genre)
print(s.painting_material)
print(s.sport)

s.dance()
s.dance("Word cup")
s.sing()
s.play_sport()
s.painting()


print("\n\n")
#Single Inheritance
class Old_painter(Artist):
    def __init__(self, paint_material, paint_brush):
        #super().__init__(paint_material)
        #super(Old_painter, self).__init__(paint_material)
        Artist.__init__(self, paint_material)
        self.paint_brush = paint_brush

x = Old_painter("Mateial x", "Brush Y")
print(x.painting_material)
x.painting()

print("\n\n")

print(help(SuperHuman))


