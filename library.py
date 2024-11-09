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
