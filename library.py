import uuid, json, ast, re
from datetime import datetime

from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author

class Library:
  def __init__(self):
    self.books = {}
    self.checkedout_books = []
    self.users = {}
    self.authors = {}
    
  def __repr__(self):
       print(str(self.books))
    
  def add_book(self):
    
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN number of the book: ")
    publication_date = input("Enter the publication date in the format of MM/DD/YYYY: ")
    genre = input("Enter the genre of the book. Type 'fiction', 'non-fiction' or 'none': ")
    sub_genre = input("Enter the sub-genre of the book: ")
    
    string_regex = r"[a-zA-Z0-9]{3,}"
    date_regex = r"\d{2}/\d{2}/\d{3,4}"
    # For simplicity of creation of a book data, no regex validation is used for ISBN (ISBN-13 digits)
    # Concatenate string to check re.match() with multiple strings
    valid_title = re.match(string_regex, title)
    valid_author = re.match(string_regex, author)
    
    valid_date = re.match(date_regex, publication_date) 
    
    
    if valid_title and valid_author and valid_date:
       if genre == "fiction":
          new_book = FictionBook(title, author, isbn, publication_date, sub_genre)
          self.books[isbn] = new_book
      
       elif genre == "non-fiction":
          new_book = NonFictionBook(title, author, isbn, publication_date, sub_genre)
          self.books[isbn] = new_book
       else:
          new_book = Book(title, author, isbn, publication_date)
          self.books[isbn] = new_book
    
    else:
      print("\033[31m", "Book title, author, genre, and subgenre has to be at least 3 characters and date has to be in valid format and refers to the past date", '\033[0m')
       

  def display_books(self):
    for isbn, book in self.books.items():
      if isinstance(book, FictionBook) or isinstance(book, NonFictionBook):
          print("\033[92m", {
            isbn: {
                'title': book.get_title(),
                'author': book.get_author(),
                'ISBN': book.get_isbn(),
                'publication_date': book.get_publication_date(),
                'genre': book.get_genre() or '',  
                'sub_genre': book.get_sub_genre() or ''  
            }
              },"\033[0m")
      else:
        print("\033[92m",{
            isbn: {
                'title': book.get_title(),
                'author': book.get_author(),
                'ISBN': book.get_isbn(),
                'publication_date': book.get_publication_date(),
                'genre': '',  
                'sub_genre': ''  
            }
              },"\033[0m")
        
























# id = str(uuid.uuid4())