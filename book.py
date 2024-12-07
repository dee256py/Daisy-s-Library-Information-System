
from deez_library import LibraryItem


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, genre: int):
        super().__init__(title, author, year)
        self.__genre = genre

    #A function that allows a patron to borrow a book
    def borrow(self):
        if self.is_available():
            self.mark_as_borrowed()
            print("You have now borrowed the book:" + {self.get_details()})
        else:
            print("This book is currently not available.") 

    def return_item(self):
        self.mark_as_available()
        print("You have returned the book:" + {self.get_details()})