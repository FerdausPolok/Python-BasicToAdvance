#composition means use another class object inside a class
class StoryBook:
    # Class Variable
    no_of_books = 0
    dicount = 0.5

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

class Library:
    def __init__(self, book_list= None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_books(self):
        for book in self.book_list:
            print(f"Title: {book.name}, AUthor: {book.author_name}, Price: {book.price}")
    def add_book(self, book):
        self.book_list.append(book)
    def remove_book(self, book):
        self.book_list.remove(book)

book_1 = StoryBook("A", 100, "B", 1955, 200)
book_2 = StoryBook("B", 200, "C", 1966, 300)

public_library = Library()

public_library.add_book(book_1)
public_library.add_book(book_2)

public_library.get_all_books()

public_library.remove_book(book_2)
public_library.get_all_books()

