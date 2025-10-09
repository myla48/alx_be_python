from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)

    # Demonstrating the __repr__ method
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()


from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ == "__main__":
    main()
