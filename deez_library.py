from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = True 

    def is_available(self):
        return self.__status

    def mark_as_borrowed(self):
        self.__status = False

    def mark_as_available(self):
        self.__status = True

    def get_details(self):
        # refactor this code and write the complete conditional statements and print statements
        return f"{self.__title} by {self.__author} ({self.__year}) - {'Available' if self.__status else 'Borrowed'}"
    
    #add getters and setter for all private attributes/properties

#Class Book inherits Library Item
class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, genre: int):
        super().__init__(title, author, year)
        self.__genre = genre

    #A function that allows a patron to borrow a book
    def borrow(self):
        if self.is_available():
            self.mark_as_borrowed()
            return f"You have borrowed the book: {self.get_details()}"
        else:
            return "This book is currently not available."

    def return_item(self):
        self.mark_as_available()
        return f"You have returned the book: {self.get_details()}"

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.__issue_number = issue_number

    def borrow(self):
        if self.is_available():
            self.mark_as_borrowed()
            return f"You have borrowed the magazine: {self.get_details()}"
        else:
            return "This magazine is currently not available."

    def return_item(self):
        self.mark_as_available()
        return f"You have returned the magazine: {self.get_details()}"

class Person:
    def __init__(self, name, patron_id):
        self.__name = name
        self.__patron_id = patron_id #move patronid attribute into patron class

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__patron_id

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name, patron_id)
        self.__borrowed_items = []

    def borrow_item(self, item):
        result = item.borrow()
        if "borrowed" in result:
            self.__borrowed_items.append(item)
        return result

    def return_item(self, item):
        result = item.return_item()
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)
        return result

    def view_borrowed_items(self):
        return [item.get_details() for item in self.__borrowed_items]

class Library:
    def __init__(self):
        self.__items = []
        self.__patrons = []

    def add_item(self, item):
        self.__items.append(item)

    def add_patron(self, patron):
        self.__patrons.append(patron)

    def lend_item_to_patron(self, item, patron):
        if item in self.__items and patron in self.__patrons:
            return patron.borrow_item(item)
        return "Item or patron not found in the library."

    def accept_returned_item(self, item, patron):
        if item in self.__items and patron in self.__patrons:
            return patron.return_item(item)
        return "Item or patron not found in the library."


    