"""
Library class to manage books and members.
"""

from exceptions import BookNotFoundError, BookNotAvailableError, MemberNotFoundError

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member with ID {member_id} not found.")
        if book_id not in self.books:
            raise BookNotFoundError(f"Book with ID {book_id} not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.available:
            raise BookNotAvailableError(f"Book '{book.title}' is not available.")

        book.mark_borrowed()
        member.borrow_book(book)

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member with ID {member_id} not found.")
        if book_id not in self.books:
            raise BookNotFoundError(f"Book with ID {book_id} not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        book.mark_returned()
        member.return_book(book_id)
