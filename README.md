

# Library Management System
This is a Python-based library management system that allows users to manage books, users, and authors, including adding new entries, borrowing, and returning books. The system supports both fiction and non-fiction books and maintains records of current loans.

## Features
Add new users to the library.
Add new books with details such as title, author, ISBN, publication date, genre, and sub-genre.
Display all users and books in the library.
Check out and return books.
Search for books by ISBN or title.
Display all current book loans.


## Usage:
**Adding a User**
To add a user, use the add_user method. You will be prompted to enter the user's name and library ID.

**Displaying Users**
To display all users, use the display_users method.

**Adding a Book**
To add a book, use the add_book method. You will need to enter the book's title, author, ISBN, publication date, genre, and sub-genre.

**Displaying Books**
To display all books, use the display_books method.

**Checking Out a Book**
To check out a book, use the checkout_book method. You will need to enter the book's ISBN and the user's library ID.

**Returning a Book**
To return a book, use the checkin_book method. You will need to enter the book's ISBN and the user's library ID.

**Displaying Borrowed Books**
To display all currently borrowed books, use the display_borrower_users method.

**Searching for a Book**
To search for a book, use the search_book method. You can search by ISBN or title.


## Class Definitions
## CopyrightLibrary
This class handles the main operations of the library.

**add_user():** Adds a new user to the library.
**display_users():** Displays all users in the library.
**add_book():** Adds a new book to the library.
**display_books():** Displays all books in the library.
**checkout_book():** Checks out a book to a user.
**checkin_book():** Returns a book to the library.
display_borrower_users(): Displays all currently borrowed books.
**search_book():** Searches for a book by ISBN or title.
## Book, FictionBook, NonFictionBook
These classes represent books in the library.

**Book:** Represents a general book.
**FictionBook:** Represents a fiction book.
**NonFictionBook:** Represents a non-fiction book.
**User**
This class represents a user of the library.

**User:** Represents a library user with attributes like name, library ID, and borrowed books.
**Author**
This class represents an author in the library system.

Author: Represents an author with attributes like name and a list of books they've written.

# Note: 
Please note that library_id should be registered in order to be able to checkout the book
The code for adding and displaying the author should be similar to user.