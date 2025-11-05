#!/usr/bin/env python3
"""
Edge Case Testing for Library Management System
Tests various edge cases and error conditions.
"""

from library_system import LibraryManagementSystem


def test_empty_library():
    """Test operations on empty library."""
    print("="*100)
    print("TEST: Empty Library Operations")
    print("="*100)
    
    library = LibraryManagementSystem()
    
    # Test display on empty library
    print("\n1. Display empty library:")
    library.display_all_books()
    
    # Test search on empty library
    print("\n2. Search in empty library:")
    book = library.search_book_by_id(1)
    print(f"   Search result: {book}")
    
    # Test remove from empty library
    print("\n3. Remove from empty library:")
    result = library.remove_book(1)
    print(f"   Remove result: {result}")
    
    # Test borrow from empty library
    print("\n4. Borrow from empty library:")
    success, message = library.borrow_book(1, "Test User")
    print(f"   Success: {success}, Message: {message}")
    
    print("\n✓ Empty library tests completed\n")


def test_single_book():
    """Test operations with single book."""
    print("="*100)
    print("TEST: Single Book Operations")
    print("="*100)
    
    library = LibraryManagementSystem()
    book = library.add_book("Test Book", "Test Author", "123-456")
    
    print(f"\n1. Added book: {book.title} (ID: {book.book_id})")
    
    # Test search
    print("\n2. Search for the book:")
    found = library.search_book_by_id(1)
    print(f"   Found: {found.title if found else 'Not found'}")
    
    # Test borrow
    print("\n3. Borrow the book:")
    success, message = library.borrow_book(1, "User1")
    print(f"   {message}")
    
    # Test return
    print("\n4. Return the book:")
    success, message = library.return_book(1)
    print(f"   {message}")
    
    # Test remove
    print("\n5. Remove the book:")
    result = library.remove_book(1)
    print(f"   Removed: {result}")
    print(f"   Library size: {library.books.get_size()}")
    
    print("\n✓ Single book tests completed\n")


def test_duplicate_operations():
    """Test duplicate operations."""
    print("="*100)
    print("TEST: Duplicate Operations")
    print("="*100)
    
    library = LibraryManagementSystem()
    book = library.add_book("Test Book", "Test Author", "123-456")
    
    print(f"\n1. Added book: {book.title}")
    
    # Try to borrow twice
    print("\n2. Borrow book twice:")
    success1, message1 = library.borrow_book(1, "User1")
    print(f"   First borrow: {message1}")
    success2, message2 = library.borrow_book(1, "User2")
    print(f"   Second borrow: {message2}")
    
    # Try to return twice
    print("\n3. Return book twice:")
    success1, message1 = library.return_book(1)
    print(f"   First return: {message1}")
    success2, message2 = library.return_book(1)
    print(f"   Second return: {message2}")
    
    print("\n✓ Duplicate operation tests completed\n")


def test_nonexistent_operations():
    """Test operations on non-existent books."""
    print("="*100)
    print("TEST: Non-existent Book Operations")
    print("="*100)
    
    library = LibraryManagementSystem()
    library.add_book("Book 1", "Author 1", "111")
    library.add_book("Book 2", "Author 2", "222")
    
    print("\n1. Search for non-existent book ID 999:")
    book = library.search_book_by_id(999)
    print(f"   Result: {book}")
    
    print("\n2. Remove non-existent book ID 999:")
    result = library.remove_book(999)
    print(f"   Result: {result}")
    
    print("\n3. Borrow non-existent book ID 999:")
    success, message = library.borrow_book(999, "User")
    print(f"   Success: {success}, Message: {message}")
    
    print("\n4. Return non-existent book ID 999:")
    success, message = library.return_book(999)
    print(f"   Success: {success}, Message: {message}")
    
    print("\n✓ Non-existent book tests completed\n")


def test_search_variations():
    """Test various search scenarios."""
    print("="*100)
    print("TEST: Search Variations")
    print("="*100)
    
    library = LibraryManagementSystem()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "111")
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "222")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "333")
    
    print("\n1. Search by partial title 'The':")
    results = library.search_books_by_title("The")
    print(f"   Found {len(results)} books")
    for book in results:
        print(f"   - {book.title}")
    
    print("\n2. Search by non-existent title:")
    results = library.search_books_by_title("Nonexistent")
    print(f"   Found {len(results)} books")
    
    print("\n3. Search by case-insensitive author:")
    results = library.search_books_by_author("harper")
    print(f"   Found {len(results)} books")
    for book in results:
        print(f"   - {book.title} by {book.author}")
    
    print("\n4. Search by ISBN:")
    book = library.search_book_by_isbn("222")
    print(f"   Found: {book.title if book else 'Not found'}")
    
    print("\n✓ Search variation tests completed\n")


def test_linked_list_integrity():
    """Test linked list maintains integrity after operations."""
    print("="*100)
    print("TEST: Linked List Integrity")
    print("="*100)
    
    library = LibraryManagementSystem()
    
    # Add multiple books
    print("\n1. Adding 5 books:")
    for i in range(1, 6):
        library.add_book(f"Book {i}", f"Author {i}", f"ISBN-{i}")
    print(f"   Total books: {library.books.get_size()}")
    
    # Remove middle book
    print("\n2. Remove middle book (ID 3):")
    library.remove_book(3)
    print(f"   Total books: {library.books.get_size()}")
    
    # Verify remaining books
    print("\n3. Verify remaining books:")
    all_books = library.books.get_all_books()
    for book in all_books:
        print(f"   - ID {book.book_id}: {book.title}")
    
    # Remove first book
    print("\n4. Remove first book (ID 1):")
    library.remove_book(1)
    print(f"   Total books: {library.books.get_size()}")
    
    # Remove last book
    print("\n5. Remove last book (ID 5):")
    library.remove_book(5)
    print(f"   Total books: {library.books.get_size()}")
    
    # Verify final state
    print("\n6. Final state:")
    all_books = library.books.get_all_books()
    for book in all_books:
        print(f"   - ID {book.book_id}: {book.title}")
    
    print("\n✓ Linked list integrity tests completed\n")


def main():
    """Run all edge case tests."""
    print("\n" + "="*100)
    print(" "*30 + "LIBRARY MANAGEMENT SYSTEM")
    print(" "*35 + "EDGE CASE TESTING")
    print("="*100 + "\n")
    
    test_empty_library()
    test_single_book()
    test_duplicate_operations()
    test_nonexistent_operations()
    test_search_variations()
    test_linked_list_integrity()
    
    print("="*100)
    print(" "*30 + "ALL EDGE CASE TESTS COMPLETED!")
    print("="*100 + "\n")


if __name__ == "__main__":
    main()
