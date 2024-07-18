class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            raise ValueError("Book is already checked out.")
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            raise ValueError("Book was not checked out.")
        self._is_checked_out = False
    
    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"
