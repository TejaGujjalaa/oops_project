"""
Main entry point for Library Management System.
"""
from library import Library
from book import Book
from member import Member
from report import available_books, borrowed_books, member_report
from utils import generate_id
from exceptions import BookNotFoundError, BookNotAvailableError, MemberNotFoundError

def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Reports")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book_id = generate_id("BOOK")
                library.add_book(Book(book_id, title, author))
                print(f"Book added with ID {book_id}")

            elif choice == "2":
                name = input("Enter member name: ")
                member_id = generate_id("MEM")
                library.add_member(Member(member_id, name))
                print(f"Member added with ID {member_id}")

            elif choice == "3":
                mem_id = input("Enter member ID: ")
                bk_id = input("Enter book ID: ")
                library.borrow_book(mem_id, bk_id)
                print(" Book borrowed successfully.")

            elif choice == "4":
                mem_id = input("Enter member ID: ")
                bk_id = input("Enter book ID: ")
                library.return_book(mem_id, bk_id)
                print(" Book returned successfully.")

            elif choice == "5":
                available_books(library)
                borrowed_books(library)
                for mem in library.members.values():
                    member_report(mem)

            elif choice == "6":
                print(" Exiting Library System. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except (BookNotFoundError, BookNotAvailableError, MemberNotFoundError) as e:
            print(f" {e}")

if __name__ == "__main__":
    main()
