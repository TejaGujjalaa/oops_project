"""
Member class representing a library member.
"""

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book_id):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                self.borrowed_books.remove(book)
                return

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member[{self.member_id}] - {self.name}, Borrowed: {borrowed_titles}"
