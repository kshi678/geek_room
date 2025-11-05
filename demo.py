#!/usr/bin/env python3
"""
Library Management System - Automated Demo
Demonstrates the key features of the system.
"""

from library_system import LibraryManagementSystem


def print_section(title):
    """Print a section header."""
    print("\n" + "="*100)
    print(f" {title}")
    print("="*100)


def main():
    """Run automated demo."""
    print_section("LIBRARY MANAGEMENT SYSTEM - AUTOMATED DEMO")
    
    # Initialize library
    library = LibraryManagementSystem()
    
    # Demo 1: Add books
    print_section("1. ADDING BOOKS TO LIBRARY")
    books_data = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
        ("To Kill a Mockingbird", "Harper Lee", "978-0061120084"),
        ("1984", "George Orwell", "978-0451524935"),
        ("Pride and Prejudice", "Jane Austen", "978-0141439518"),
        ("The Catcher in the Rye", "J.D. Salinger", "978-0316769174")
    ]
    
    for title, author, isbn in books_data:
        book = library.add_book(title, author, isbn)
        print(f"✓ Added: {book.title} by {book.author} (ID: {book.book_id})")
    
    # Demo 2: Display all books
    print_section("2. DISPLAYING ALL BOOKS")
    library.display_all_books()
    
    # Demo 3: Search by title
    print_section("3. SEARCHING BOOKS BY TITLE")
    search_term = "The"
    print(f"Searching for books with '{search_term}' in title:")
    results = library.search_books_by_title(search_term)
    print(f"\nFound {len(results)} book(s):")
    for book in results:
        print(f"  - {book.title} by {book.author}")
    
    # Demo 4: Search by author
    print_section("4. SEARCHING BOOKS BY AUTHOR")
    author_search = "Harper"
    print(f"Searching for books by author containing '{author_search}':")
    results = library.search_books_by_author(author_search)
    for book in results:
        print(f"  - {book.title} by {book.author}")
    
    # Demo 5: Borrow books
    print_section("5. BORROWING BOOKS")
    borrowers = [
        (1, "Alice Johnson"),
        (3, "Bob Smith"),
        (5, "Charlie Brown")
    ]
    
    for book_id, borrower in borrowers:
        success, message = library.borrow_book(book_id, borrower)
        print(f"{'✓' if success else '✗'} {message}")
    
    # Demo 6: Display available books
    print_section("6. DISPLAYING AVAILABLE BOOKS")
    library.display_available_books()
    
    # Demo 7: Display borrowed books
    print_section("7. DISPLAYING BORROWED BOOKS")
    library.display_borrowed_books()
    
    # Demo 8: Return a book
    print_section("8. RETURNING A BOOK")
    return_id = 1
    success, message = library.return_book(return_id)
    print(f"{'✓' if success else '✗'} {message}")
    
    # Demo 9: Try to borrow already borrowed book
    print_section("9. ATTEMPTING TO BORROW ALREADY BORROWED BOOK")
    success, message = library.borrow_book(3, "David Wilson")
    print(f"{'✗' if not success else '✓'} {message}")
    
    # Demo 10: Library statistics
    print_section("10. LIBRARY STATISTICS")
    stats = library.get_statistics()
    print(f"Total Books: {stats['total']}")
    print(f"Available Books: {stats['available']}")
    print(f"Borrowed Books: {stats['borrowed']}")
    
    # Demo 11: Remove a book
    print_section("11. REMOVING A BOOK")
    remove_id = 4
    book = library.search_book_by_id(remove_id)
    if book:
        print(f"Removing: {book.title} (ID: {remove_id})")
        success = library.remove_book(remove_id)
        print(f"{'✓' if success else '✗'} Book removed successfully" if success else "Failed to remove book")
    
    # Demo 12: Final state
    print_section("12. FINAL LIBRARY STATE")
    library.display_all_books()
    
    # Final statistics
    print_section("FINAL STATISTICS")
    stats = library.get_statistics()
    print(f"Total Books: {stats['total']}")
    print(f"Available Books: {stats['available']}")
    print(f"Borrowed Books: {stats['borrowed']}")
    
    print_section("DEMO COMPLETED SUCCESSFULLY!")
    print("\nTo run the interactive application, execute: python3 main.py")
    print("="*100 + "\n")


if __name__ == "__main__":
    main()
