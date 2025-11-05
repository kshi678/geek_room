class Book:
    """
    Represents a book in the library system.
    """
    
    def __init__(self, book_id, title, author, isbn):
        """
        Initialize a Book object.
        
        Args:
            book_id (int): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN number of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None
    
    def borrow(self, borrower_name):
        """
        Mark the book as borrowed.
        
        Args:
            borrower_name (str): Name of the person borrowing the book
            
        Returns:
            bool: True if successful, False if already borrowed
        """
        if self.is_available:
            self.is_available = False
            self.borrowed_by = borrower_name
            return True
        return False
    
    def return_book(self):
        """
        Mark the book as returned.
        
        Returns:
            bool: True if successful, False if not borrowed
        """
        if not self.is_available:
            self.is_available = True
            self.borrowed_by = None
            return True
        return False
    
    def __str__(self):
        """
        String representation of the book.
        """
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}"
    
    def __repr__(self):
        return self.__str__()
