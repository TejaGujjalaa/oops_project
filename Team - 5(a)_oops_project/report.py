"""
Reporting functions.
"""

def available_books(library):
    print("\n Available Books:")
    found = False
    for book in library.books.values():
        if book.available:
            print(f"  - {book}")
            found = True
    if not found:
        print(" No books available right now.")

def borrowed_books(library):
    print("\n Borrowed Books:")
    found = False
    for book in library.books.values():
        if not book.available:
            print(f"  - {book}")
            found = True
    if not found:
        print("   No books are currently borrowed.")

def member_report(member):
    print(f"\n Member Report: {member.name} (ID: {member.member_id})")
    if not member.borrowed_books:
        print("  No borrowed books.")
    else:
        for book in member.borrowed_books:
            print(f"    - {book}")
