"""
Book class representing a library book.

Attributes:
- book_id (str)
- title (str)
- author (str)
- available (bool)

Methods:
- mark_borrowed()
- mark_returned()
- __str__()
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def mark_borrowed(self):
        self.available = False

    def mark_returned(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"
