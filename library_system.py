from book import Book
from linked_list import LinkedList


class LibraryManagementSystem:
    """
    Main Library Management System class that manages all library operations.
    """
    
    def __init__(self):
        """
        Initialize the Library Management System.
        """
        self.books = LinkedList()
        self.next_book_id = 1
    
    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.
        
        Args:
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
            
        Returns:
            Book: The newly created book object
        """
        book = Book(self.next_book_id, title, author, isbn)
        self.books.insert_at_end(book)
        self.next_book_id += 1
        return book
    
    def remove_book(self, book_id):
        """
        Remove a book from the library by ID.
        
        Args:
            book_id (int): ID of the book to remove
            
        Returns:
            bool: True if removed, False if not found
        """
        return self.books.delete_by_id(book_id)
    
    def search_book_by_id(self, book_id):
        """
        Search for a book by ID.
        
        Args:
            book_id (int): ID of the book
            
        Returns:
            Book: The book object if found, None otherwise
        """
        return self.books.search_by_id(book_id)
    
    def search_books_by_title(self, title):
        """
        Search for books by title.
        
        Args:
            title (str): Title to search for
            
        Returns:
            list: List of matching books
        """
        return self.books.search_by_title(title)
    
    def search_books_by_author(self, author):
        """
        Search for books by author.
        
        Args:
            author (str): Author to search for
            
        Returns:
            list: List of matching books
        """
        return self.books.search_by_author(author)
    
    def search_book_by_isbn(self, isbn):
        """
        Search for a book by ISBN.
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Book: The book object if found, None otherwise
        """
        return self.books.search_by_isbn(isbn)
    
    def borrow_book(self, book_id, borrower_name):
        """
        Borrow a book from the library.
        
        Args:
            book_id (int): ID of the book to borrow
            borrower_name (str): Name of the borrower
            
        Returns:
            tuple: (success: bool, message: str)
        """
        book = self.books.search_by_id(book_id)
        
        if book is None:
            return False, "Book not found."
        
        if book.borrow(borrower_name):
            return True, f"Book '{book.title}' borrowed successfully by {borrower_name}."
        else:
            return False, f"Book '{book.title}' is already borrowed by {book.borrowed_by}."
    
    def return_book(self, book_id):
        """
        Return a borrowed book to the library.
        
        Args:
            book_id (int): ID of the book to return
            
        Returns:
            tuple: (success: bool, message: str)
        """
        book = self.books.search_by_id(book_id)
        
        if book is None:
            return False, "Book not found."
        
        if book.return_book():
            return True, f"Book '{book.title}' returned successfully."
        else:
            return False, f"Book '{book.title}' was not borrowed."
    
    def display_all_books(self):
        """
        Display all books in the library.
        """
        if self.books.is_empty():
            print("\nNo books in the library.")
        else:
            print(f"\nTotal Books: {self.books.get_size()}")
            self.books.display()
    
    def display_available_books(self):
        """
        Display all available books.
        """
        available_books = self.books.get_available_books()
        
        if not available_books:
            print("\nNo available books.")
        else:
            print(f"\nAvailable Books: {len(available_books)}")
            print("\n" + "="*100)
            for book in available_books:
                print(book)
            print("="*100)
    
    def display_borrowed_books(self):
        """
        Display all borrowed books.
        """
        borrowed_books = self.books.get_borrowed_books()
        
        if not borrowed_books:
            print("\nNo borrowed books.")
        else:
            print(f"\nBorrowed Books: {len(borrowed_books)}")
            print("\n" + "="*100)
            for book in borrowed_books:
                print(book)
            print("="*100)
    
    def get_statistics(self):
        """
        Get library statistics.
        
        Returns:
            dict: Dictionary containing statistics
        """
        total = self.books.get_size()
        available = len(self.books.get_available_books())
        borrowed = len(self.books.get_borrowed_books())
        
        return {
            'total': total,
            'available': available,
            'borrowed': borrowed
        }
