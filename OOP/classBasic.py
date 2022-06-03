class StoryBook:
    # Class Variable
    no_of_books = 0
    dicount = 0.7

    def __init__(self, name, price, author_name, author_born, no_of_pages):  # constructor
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishing_year = 2020
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    # regular method
    def get_book_info(self):
        print(f"The name of the book is {self.name} and it has {self.no_of_pages} pages")

    # applying discount to an instance regular method
    def apply_discount(self):
        self.price = int(self.price - self.price * self.dicount)

    # Method to change price
    def change_price(self, new_price):
        self.price = new_price

    # Class Method-1
    @classmethod
    def set_dicount(cls, new_discount):
        cls.dicount = new_discount

    # Class Method -2 (Use as an constructor)
    @classmethod
    def contruct_from_string(cls, book_str):
        name, price, author_name, author_born, pages = book_str.split(',')
        return cls(name, price, author_name, author_born, pages)

    #Static Method (Which methods can not be changed/ we dont use class or instance)

    @staticmethod
    def is_new(publishing_year):
        if publishing_year>2016:
            print("It's  a new Book")
        else:
            ("It's not a new Book")





# Creating object of story book class

book1 = StoryBook("A", 200, "Mr.X", 1998, 100)
book2 = StoryBook("B", "201", "Mr. Y", "1999", 200)

print(book1.price)
print(book2.price)

print(type(book1.price))
print(type(book2.price))

book1.name = "Lolipop"

print(book1.name)
print(book1.publishing_year)

# calling regular method using object
book1.get_book_info()

# calling regular method using class
StoryBook.get_book_info(book2)

# using class variable

print(book1.no_of_books)
print(book2.no_of_books)
print(StoryBook.no_of_books)

print(book1.price)
book1.apply_discount()
print(book1.price)
book1.dicount = 0.7
book1.apply_discount()
print(book1.price)

book1.price = 100  # not recomanded
print(book1.price)

book1.change_price(10)  # recomanded
print(book1.price)

print(book1.dicount)
StoryBook.set_dicount(0.5)
print(StoryBook.dicount)
book1.apply_discount()
print(book1.price)

#getting a str from any database or api
book_str= 'Harry Potter, 200 , Jk Rowling, 1970, 400'
name, price, author_name, author_born, pages = book_str.split(',')
harry_potter = StoryBook(name, price,author_name,author_born,pages)
print(harry_potter.name)

#We can do the same task using class methods

book_str= 'Harry Potter-2, 400 , Jk Rowling-2, 1970-2, 400-2'
harry_potter2 = StoryBook.contruct_from_string(book_str)
print(harry_potter2.name)

#use of static method
print(book1.publishing_year)
StoryBook.is_new(book1.publishing_year)