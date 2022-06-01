class StoryBook:
    #Class Variable
    no_of_books = 0
    dicount = 0.5
    def __init__(self, name, price, author_name,author_born,no_of_pages): #constructor
        self.name = name
        self.price = price
        self.author_name= author_name
        self.author_born = author_born
        self.publishing_year=2020
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    #regular method
    def get_book_info(self):
        print(f"The name of the book is {self.name} and it has {self.no_of_pages} pages")

    #applying discount to an instance regular method
    def apply_discount(self):
        self.price = int(self.price - self.price * self.dicount)

#Creating object of story book class

book1 = StoryBook("A", 200, "Mr.X", 1998, 100)
book2 = StoryBook("B", "201", "Mr. Y", "1999", 200)

print(book1.price)
print(book2.price)

print(type(book1.price))
print(type(book2.price))

book1.name ="Lolipop"

print(book1.name)
print(book1.publishing_year)

#calling regular method using object
book1.get_book_info()

#calling regular method using class
StoryBook.get_book_info(book2)

#using class variable

print(book1.no_of_books)
print(book2.no_of_books)
print(StoryBook.no_of_books)

print(book1.price)
book1.apply_discount()
print(book1.price)
book1.dicount= 0.7
book1.apply_discount()
print(book1.price)
