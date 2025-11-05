# 🚀 Quick Start Guide - Library Management System

## ⚡ Quick Commands

### Run the Interactive Application
```bash
python3 main.py
```

### Run Automated Demo
```bash
python3 demo.py
```

### Run All Tests
```bash
python3 test_edge_cases.py
```

---

## 📚 What This Project Does

A **Library Management System** that uses a custom **Linked List** data structure to manage books. No built-in Python lists or dictionaries are used for core storage!

### Key Features:
- ✅ Add/Remove books
- ✅ Search by ID, Title, Author, or ISBN
- ✅ Borrow and return books
- ✅ Track who borrowed what
- ✅ View statistics
- ✅ Filter available/borrowed books

---

## 🎯 Main Menu Options

When you run `python3 main.py`, you'll see:

```
1.  Add a New Book          - Add books with auto-generated IDs
2.  Remove a Book           - Remove by book ID
3.  Search Book by ID       - Find specific book
4.  Search Books by Title   - Partial match, case-insensitive
5.  Search Books by Author  - Partial match, case-insensitive
6.  Search Book by ISBN     - Exact ISBN match
7.  Borrow a Book          - Borrow available books
8.  Return a Book          - Return borrowed books
9.  Display All Books      - Show everything
10. Display Available Books - Show only available
11. Display Borrowed Books  - Show only borrowed
12. View Library Statistics - See the numbers
0.  Exit                   - Quit application
```

---

## 💡 Example Usage

### Adding a Book
```
Choice: 1
Enter book title: The Great Gatsby
Enter author name: F. Scott Fitzgerald
Enter ISBN: 978-0743273565
✓ Book added successfully! (ID: 1)
```

### Searching by Title
```
Choice: 4
Enter title: Gatsby
✓ Found 1 book(s):
  ID: 1 | Title: The Great Gatsby | Author: F. Scott Fitzgerald
```

### Borrowing a Book
```
Choice: 7
Enter book ID: 1
Enter your name: John Doe
✓ Book 'The Great Gatsby' borrowed successfully by John Doe.
```

### Returning a Book
```
Choice: 8
Enter book ID: 1
✓ Book 'The Great Gatsby' returned successfully.
```

---

## 🏗️ Project Architecture

```
Book Class (book.py)
    ↓
Node Class (linked_list.py)
    ↓
LinkedList Class (linked_list.py)
    ↓
LibraryManagementSystem (library_system.py)
    ↓
CLI Interface (main.py)
```

---

## 🧪 Testing

All tests have been verified and passed:
- ✅ Empty library operations
- ✅ Single book operations
- ✅ Duplicate operation prevention
- ✅ Non-existent book handling
- ✅ Search variations
- ✅ Linked list integrity

**Test Success Rate: 100%** 🎉

---

## 📊 Project Files

| File | Purpose | Lines |
|------|---------|-------|
| `book.py` | Book class definition | ~60 |
| `linked_list.py` | Custom linked list implementation | ~200 |
| `library_system.py` | Main system logic | ~150 |
| `main.py` | Interactive CLI interface | ~250 |
| `test_edge_cases.py` | Comprehensive testing | ~250 |
| `demo.py` | Automated demonstration | ~150 |
| `README.md` | Full documentation | ~300 |

**Total: ~1,360 lines of code**

---

## 🎓 Educational Value

This project demonstrates:
1. **Custom Data Structures** - Linked list from scratch
2. **OOP Principles** - Classes, encapsulation, methods
3. **Algorithm Design** - Search, insert, delete operations
4. **Error Handling** - Graceful edge case management
5. **User Interface** - Clean CLI design
6. **Testing** - Comprehensive test coverage

---

## 👥 Contributors

- Harshita Gupta (5th sem CSE)
- Rajveer Singh
- Nishant Pratap Savita (5th sem AI & ML)
- Batman

---

## 🎯 System Status

**Status:** ✅ FULLY FUNCTIONAL  
**Python Version:** 3.9.23  
**Environment:** Amazon Linux 2023  
**Last Verified:** November 5, 2025

---

## 📝 Notes

- All operations use the custom linked list (no built-in lists!)
- Book IDs are auto-generated and sequential
- Search operations are case-insensitive
- Borrowed books cannot be borrowed again until returned
- The system handles all edge cases gracefully

---

## 🚀 Ready to Use!

The system is **production-ready** for educational purposes. All features work correctly, and comprehensive testing has been completed.

**Start exploring:** `python3 main.py`

---

**Need help?** Check `README.md` for detailed documentation or run `python3 demo.py` to see all features in action!
