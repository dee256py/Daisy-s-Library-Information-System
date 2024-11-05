from deez_library import Library,Book,Magazine,Patron


def main():
    library: Library = Library()

    book1 = Book(1984, "George Orwell", 1949, "Dystopian")
    magazine1 = Magazine("Nature", "Various", 2023, "Vol 12")

        #Adding books and magazines into library shleves
    library.add_item(book1)
    library.add_item(magazine1)

    patron1 = Patron("Alice", "P1")
    patron2 = Patron("Bob", "P2")

    library.add_patron(patron1)
    library.add_patron(patron2)
    print(library.lend_item_to_patron(book1, patron1)) 
    print(library.lend_item_to_patron(magazine1, patron2)) 
    print("Alice's borrowed items:", patron1.view_borrowed_items())
    print("Bob's borrowed items:", patron2.view_borrowed_items())
    print(library.accept_returned_item(book1, patron1)) 
    print(library.accept_returned_item(magazine1, patron2))  
    print("Alice's borrowed items after return:", patron1.view_borrowed_items())
    print("Bob's borrowed items after return:", patron2.view_borrowed_items())


if __name__ == "__main__":
    main()
