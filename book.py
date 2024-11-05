
from deez_library import LibraryItem


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, genre: int):
        super().__init__(title, author, year)
        self.__genre = genre

    #A function that allows a patron to borrow a book
    def borrow(self):
        if self.is_available():
            self.mark_as_borrowed()
            return f"You have now borrowed the book: {self.get_details()}"
        else:
            return "This book is currently not available."

    def return_item(self):
        self.mark_as_available()
        return f"You have returned the book: {self.get_details()}"