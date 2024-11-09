from deez_library import Person

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
