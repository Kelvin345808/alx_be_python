class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """
        Initialize a Book instance.

        :param title: str, title of the book
        :param author: str, author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Mark the book as checked out if it is available.

        :return: bool, True if the book was successfully checked out, False otherwise
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Mark the book as available (returned).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Check if the book is available.

        :return: bool, True if the book is not checked out, False otherwise
        """
        return not self._is_checked_out


class Library:
    """A class to represent a library that manages books."""

    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Add a book to the library.

        :param book: Book instance to add
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.

        :param title: str, title of the book to check out
        :return: None
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """
        Return a book by title.

        :param title: str, title of the book to return
        :return: None
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"Successfully returned '{title}'.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """
        List all books that are currently available.

        :return: None
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
