#!/usr/bin/env python3
"""
Library Management System - Main Application
A command-line interface for managing library books using a linked list data structure.
"""

from library_system import LibraryManagementSystem


def print_header():
    """Print the application header."""
    print("\n" + "="*100)
    print(" "*35 + "LIBRARY MANAGEMENT SYSTEM")
    print(" "*30 + "(Implemented using Linked List)")
    print("="*100)


def print_menu():
    """Print the main menu."""
    print("\n" + "-"*100)
    print("MAIN MENU:")
    print("-"*100)
    print("1.  Add a New Book")
    print("2.  Remove a Book")
    print("3.  Search Book by ID")
    print("4.  Search Books by Title")
    print("5.  Search Books by Author")
    print("6.  Search Book by ISBN")
    print("7.  Borrow a Book")
    print("8.  Return a Book")
    print("9.  Display All Books")
    print("10. Display Available Books")
    print("11. Display Borrowed Books")
    print("12. View Library Statistics")
    print("0.  Exit")
    print("-"*100)


def add_book(library):
    """Add a new book to the library."""
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN: ").strip()
    
    if not title or not author or not isbn:
        print("Error: All fields are required!")
        return
    
    book = library.add_book(title, author, isbn)
    print(f"\n✓ Book added successfully!")
    print(f"  Book ID: {book.book_id}")
    print(f"  Title: {book.title}")
    print(f"  Author: {book.author}")
    print(f"  ISBN: {book.isbn}")


def remove_book(library):
    """Remove a book from the library."""
    print("\n--- Remove Book ---")
    try:
        book_id = int(input("Enter book ID to remove: "))
        
        book = library.search_book_by_id(book_id)
        if book:
            if library.remove_book(book_id):
                print(f"\n✓ Book '{book.title}' (ID: {book_id}) removed successfully!")
            else:
                print("\n✗ Failed to remove book.")
        else:
            print(f"\n✗ Book with ID {book_id} not found.")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid book ID.")


def search_by_id(library):
    """Search for a book by ID."""
    print("\n--- Search Book by ID ---")
    try:
        book_id = int(input("Enter book ID: "))
        book = library.search_book_by_id(book_id)
        
        if book:
            print("\n" + "="*100)
            print(book)
            print("="*100)
        else:
            print(f"\n✗ Book with ID {book_id} not found.")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid book ID.")


def search_by_title(library):
    """Search for books by title."""
    print("\n--- Search Books by Title ---")
    title = input("Enter title (or part of it): ").strip()
    
    if not title:
        print("\n✗ Title cannot be empty!")
        return
    
    books = library.search_books_by_title(title)
    
    if books:
        print(f"\n✓ Found {len(books)} book(s):")
        print("\n" + "="*100)
        for book in books:
            print(book)
        print("="*100)
    else:
        print(f"\n✗ No books found with title containing '{title}'.")


def search_by_author(library):
    """Search for books by author."""
    print("\n--- Search Books by Author ---")
    author = input("Enter author name (or part of it): ").strip()
    
    if not author:
        print("\n✗ Author name cannot be empty!")
        return
    
    books = library.search_books_by_author(author)
    
    if books:
        print(f"\n✓ Found {len(books)} book(s):")
        print("\n" + "="*100)
        for book in books:
            print(book)
        print("="*100)
    else:
        print(f"\n✗ No books found by author '{author}'.")


def search_by_isbn(library):
    """Search for a book by ISBN."""
    print("\n--- Search Book by ISBN ---")
    isbn = input("Enter ISBN: ").strip()
    
    if not isbn:
        print("\n✗ ISBN cannot be empty!")
        return
    
    book = library.search_book_by_isbn(isbn)
    
    if book:
        print("\n" + "="*100)
        print(book)
        print("="*100)
    else:
        print(f"\n✗ Book with ISBN '{isbn}' not found.")


def borrow_book(library):
    """Borrow a book from the library."""
    print("\n--- Borrow Book ---")
    try:
        book_id = int(input("Enter book ID to borrow: "))
        borrower_name = input("Enter your name: ").strip()
        
        if not borrower_name:
            print("\n✗ Borrower name cannot be empty!")
            return
        
        success, message = library.borrow_book(book_id, borrower_name)
        
        if success:
            print(f"\n✓ {message}")
        else:
            print(f"\n✗ {message}")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid book ID.")


def return_book(library):
    """Return a borrowed book."""
    print("\n--- Return Book ---")
    try:
        book_id = int(input("Enter book ID to return: "))
        
        success, message = library.return_book(book_id)
        
        if success:
            print(f"\n✓ {message}")
        else:
            print(f"\n✗ {message}")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid book ID.")


def view_statistics(library):
    """View library statistics."""
    print("\n--- Library Statistics ---")
    stats = library.get_statistics()
    
    print("\n" + "="*100)
    print(f"Total Books in Library: {stats['total']}")
    print(f"Available Books: {stats['available']}")
    print(f"Borrowed Books: {stats['borrowed']}")
    print("="*100)


def main():
    """Main application loop."""
    library = LibraryManagementSystem()
    
    print_header()
    print("\nWelcome to the Library Management System!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (0-12): ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_by_id(library)
        elif choice == '4':
            search_by_title(library)
        elif choice == '5':
            search_by_author(library)
        elif choice == '6':
            search_by_isbn(library)
        elif choice == '7':
            borrow_book(library)
        elif choice == '8':
            return_book(library)
        elif choice == '9':
            library.display_all_books()
        elif choice == '10':
            library.display_available_books()
        elif choice == '11':
            library.display_borrowed_books()
        elif choice == '12':
            view_statistics(library)
        elif choice == '0':
            print("\n" + "="*100)
            print("Thank you for using the Library Management System!")
            print("Goodbye!")
            print("="*100 + "\n")
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 0 and 12.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
