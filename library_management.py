# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            raise ValueError(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            raise ValueError(f"'{self.title}' was not checked out.")

    def is_checked_out(self):
        return self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not any(b.title == book.title for b in self._books):
            self._books.append(book)
        else:
            raise ValueError(f"'{book.title}' already exists in the library.")

    def check_out_book(self, title):
        book = self._find_book(title)
        if book and not book.is_checked_out():
            book.check_out()
        else:
            print(f"Book '{title}' is either not available or already checked out.")

    def return_book(self, title):
        book = self._find_book(title)
        if book and book.is_checked_out():
            book.return_book()
        else:
            print(f"Book '{title}' is either not checked out or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

    def _find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None
