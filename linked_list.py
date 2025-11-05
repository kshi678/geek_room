class Node:
    """
    Represents a node in the linked list.
    """
    
    def __init__(self, data):
        """
        Initialize a Node.
        
        Args:
            data: The data to store in the node (Book object)
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Custom Linked List implementation for storing books.
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The data to insert (Book object)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        
        Args:
            data: The data to insert (Book object)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def delete_by_id(self, book_id):
        """
        Delete a node by book ID.
        
        Args:
            book_id (int): The ID of the book to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        if self.is_empty():
            return False
        
        if self.head.data.book_id == book_id:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data.book_id == book_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search_by_id(self, book_id):
        """
        Search for a book by ID.
        
        Args:
            book_id (int): The ID of the book to search
            
        Returns:
            Book: The book object if found, None otherwise
        """
        current = self.head
        while current:
            if current.data.book_id == book_id:
                return current.data
            current = current.next
        return None
    
    def search_by_title(self, title):
        """
        Search for books by title (partial match, case-insensitive).
        
        Args:
            title (str): The title to search for
            
        Returns:
            list: List of matching books
        """
        results = []
        current = self.head
        title_lower = title.lower()
        
        while current:
            if title_lower in current.data.title.lower():
                results.append(current.data)
            current = current.next
        
        return results
    
    def search_by_author(self, author):
        """
        Search for books by author (partial match, case-insensitive).
        
        Args:
            author (str): The author to search for
            
        Returns:
            list: List of matching books
        """
        results = []
        current = self.head
        author_lower = author.lower()
        
        while current:
            if author_lower in current.data.author.lower():
                results.append(current.data)
            current = current.next
        
        return results
    
    def search_by_isbn(self, isbn):
        """
        Search for a book by ISBN.
        
        Args:
            isbn (str): The ISBN to search for
            
        Returns:
            Book: The book object if found, None otherwise
        """
        current = self.head
        while current:
            if current.data.isbn == isbn:
                return current.data
            current = current.next
        return None
    
    def get_all_books(self):
        """
        Get all books in the list.
        
        Returns:
            list: List of all books
        """
        books = []
        current = self.head
        while current:
            books.append(current.data)
            current = current.next
        return books
    
    def get_available_books(self):
        """
        Get all available books.
        
        Returns:
            list: List of available books
        """
        books = []
        current = self.head
        while current:
            if current.data.is_available:
                books.append(current.data)
            current = current.next
        return books
    
    def get_borrowed_books(self):
        """
        Get all borrowed books.
        
        Returns:
            list: List of borrowed books
        """
        books = []
        current = self.head
        while current:
            if not current.data.is_available:
                books.append(current.data)
            current = current.next
        return books
    
    def get_size(self):
        """
        Get the size of the linked list.
        
        Returns:
            int: Number of nodes in the list
        """
        return self.size
    
    def display(self):
        """
        Display all books in the list.
        """
        if self.is_empty():
            print("No books in the library.")
            return
        
        current = self.head
        print("\n" + "="*100)
        while current:
            print(current.data)
            current = current.next
        print("="*100)
