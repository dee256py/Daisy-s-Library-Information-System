from deez_library import LibraryItem

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
