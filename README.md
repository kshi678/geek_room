# Library Management System (Linked List Implementation)

A comprehensive command-line Library Management System implemented in Python using a custom **Linked List** data structure. This project demonstrates fundamental data structure concepts and object-oriented programming principles.

## 🎓 Project Contributors

- Harshita Gupta (5th sem CSE)
- Rajveer Singh
- Nishant Pratap Savita (5th sem AI & ML)
- Batman

## 📋 Features

### Core Functionality
- ✅ **Add Books** - Add new books to the library with auto-generated IDs
- ✅ **Remove Books** - Remove books from the library by ID
- ✅ **Search Operations**
  - Search by Book ID
  - Search by Title (partial match, case-insensitive)
  - Search by Author (partial match, case-insensitive)
  - Search by ISBN
- ✅ **Borrow/Return System** - Track book borrowing and returns with borrower information
- ✅ **Display Options**
  - View all books
  - View available books only
  - View borrowed books only
- ✅ **Statistics** - View library statistics (total, available, borrowed books)

### Technical Features
- Custom **Linked List** implementation (no built-in data structures used)
- **Node-based** storage for efficient insertions and deletions
- **Object-Oriented Design** with separate classes for Book, Node, LinkedList, and LibrarySystem
- **User-friendly CLI** with formatted output and error handling

## 🏗️ Project Structure

```
/vercel/sandbox/
├── book.py              # Book class definition
├── linked_list.py       # Node and LinkedList implementation
├── library_system.py    # Main LibraryManagementSystem class
├── main.py              # CLI interface and application entry point
└── README.md            # Project documentation
```

## 📦 Components

### 1. Book Class (`book.py`)
Represents a book with the following attributes:
- `book_id` - Unique identifier
- `title` - Book title
- `author` - Book author
- `isbn` - ISBN number
- `is_available` - Availability status
- `borrowed_by` - Name of current borrower (if borrowed)

### 2. Linked List (`linked_list.py`)
Custom implementation featuring:
- **Node class** - Basic linked list node
- **LinkedList class** - Complete linked list with operations:
  - Insert at beginning/end
  - Delete by ID
  - Search operations (by ID, title, author, ISBN)
  - Filter operations (available/borrowed books)
  - Display functionality

### 3. Library Management System (`library_system.py`)
Main system class that:
- Manages the book collection using LinkedList
- Handles all library operations
- Provides high-level methods for book management
- Tracks book IDs automatically

### 4. Main Application (`main.py`)
Interactive CLI featuring:
- User-friendly menu system
- Input validation
- Formatted output
- Error handling

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation
1. Clone or download the project files
2. Navigate to the project directory:
   ```bash
   cd /vercel/sandbox
   ```

### Running the Application
Execute the main program:
```bash
python3 main.py
```

## 📖 Usage Guide

### Main Menu Options

```
1.  Add a New Book          - Add a new book to the library
2.  Remove a Book           - Remove a book by ID
3.  Search Book by ID       - Find a specific book by its ID
4.  Search Books by Title   - Search books by title (partial match)
5.  Search Books by Author  - Search books by author (partial match)
6.  Search Book by ISBN     - Find a book by its ISBN
7.  Borrow a Book          - Borrow an available book
8.  Return a Book          - Return a borrowed book
9.  Display All Books      - Show all books in the library
10. Display Available Books - Show only available books
11. Display Borrowed Books  - Show only borrowed books
12. View Library Statistics - View library statistics
0.  Exit                   - Exit the application
```

### Example Workflow

1. **Adding a Book:**
   ```
   Enter book title: The Great Gatsby
   Enter author name: F. Scott Fitzgerald
   Enter ISBN: 978-0743273565
   ```

2. **Searching by Title:**
   ```
   Enter title (or part of it): Gatsby
   ```

3. **Borrowing a Book:**
   ```
   Enter book ID to borrow: 1
   Enter your name: John Doe
   ```

4. **Returning a Book:**
   ```
   Enter book ID to return: 1
   ```

## 🔍 Data Structure Details

### Linked List Implementation
The project uses a **singly linked list** where:
- Each node contains a Book object and a reference to the next node
- The head pointer tracks the first node
- Size is maintained for O(1) size queries
- Operations are performed by traversing the list

### Time Complexity
- **Insert at end**: O(n)
- **Insert at beginning**: O(1)
- **Delete by ID**: O(n)
- **Search operations**: O(n)
- **Display**: O(n)

### Space Complexity
- O(n) where n is the number of books

## 🎯 Key Concepts Demonstrated

1. **Data Structures**
   - Linked List implementation from scratch
   - Node-based storage
   - Dynamic memory allocation

2. **Object-Oriented Programming**
   - Encapsulation
   - Class design
   - Method organization

3. **Algorithm Design**
   - Linear search
   - List traversal
   - Node insertion/deletion

4. **Software Engineering**
   - Modular design
   - Separation of concerns
   - User interface design

## 🧪 Testing

The system has been tested for:
- ✅ Adding multiple books
- ✅ Removing books (existing and non-existing)
- ✅ Searching with various criteria
- ✅ Borrowing and returning books
- ✅ Edge cases (empty list, invalid inputs)
- ✅ Display operations
- ✅ Statistics accuracy

## 🛠️ Future Enhancements

Potential improvements:
- Persistent storage (file/database)
- Due date tracking for borrowed books
- Fine calculation for overdue books
- Multiple copies of the same book
- User account management
- Book categories/genres
- Doubly linked list for bidirectional traversal
- Sorted insertion for better search performance

## 📝 License

This is an educational project created for learning purposes.

## 👥 Contributing

This project is part of an academic assignment. Feel free to fork and modify for your own learning!

## 📧 Contact

For questions or suggestions, please contact the project contributors.

---

**Note:** This project demonstrates the implementation of a Library Management System using fundamental data structures without relying on Python's built-in list or dictionary structures for the core book storage mechanism.
