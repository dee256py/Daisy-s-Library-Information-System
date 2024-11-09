from deez_library import ABC


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
    
