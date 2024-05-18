import ast, re, json, os
from datetime import datetime
import pickle

from book import Book
from user import User
from author import Author

class Library:
  def __init__(self):
    self.books = {}
    self.users = {}  
    self.authors = {}
    self.genres = {}
    self.current_loans = {}
    
  def add_user(self):
    user_name = input("Enter the user name: ")
    library_id = input("What is the user library id? ")
    
    if not library_id or not user_name:
      print("User name and library Id is required")
      exit()
    
    if library_id not in self.users:
      user = User(user_name, library_id)
      self.users[library_id] = user
      print('\33[32m', f"User with the name {user_name} and id of {library_id} added","\033[0m")

    else:
      print('\033[91m', f"User with library id of {library_id} already exists", '\033[0m')
    
    
    
  def display_users(self):
    for library_id, user in self.users.items():
      print('\33[33m', {
        library_id: {
          'library_id': user.library_id,
          'name': user.name,
          'borrowed_books': [x.get_title() for x in user.borrowed_books]
        }
      },"\033[0m")
      
    
  def add_book(self):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN number of the book: ")
    publication_date = input("Enter the publication date in the format of MM/DD/YYYY: ")
    genre = input("Enter the genre of the book: ")
    
    string_regex = r"[a-zA-Z0-9 .]{3,}"
    date_regex = r"\d{2}/\d{2}/\d{3,4}"
    # For simplicity of creation of a book data in cli, no regex validation is used for ISBN (ISBN-13 digits)
    valid_title = re.match(string_regex, title)
    valid_author = re.match(string_regex, author)
    valid_date = re.match(date_regex, publication_date) 
    
    if valid_title and valid_author and valid_date:
          new_book = Book(title, author, isbn, publication_date, genre)
          self.books[isbn] = new_book
          print("\033[92m", "Book added successfully!", "\033[0m")
      
    else:
      print("\033[31m", "Book title, author have to be at least 3 characters and date has to be in valid format and refers to the past date", '\033[0m')
       

  def display_books(self):
    output = {}
    for isbn, book in self.books.items():
          one_book = {  
            isbn: {
                'title': book.get_title(),
                'author': book.get_author(),
                'ISBN': book.get_isbn(),
                'publication_date': book.get_publication_date(),
                'is_available': book.get_is_available(),
                'genre': book.get_genre()
            }
          }
          output.update(one_book)
          
    print("\033[92m",json.dumps(output, indent=4, sort_keys=True), "\033[0m")
     
        

  def checkout_book(self):
    isbn = input("Enter the ISBN of the book to borrow: ")
    library_id = input("What is the user's id? ")
    if library_id in self.users:
      if isbn in self.books and self.books[isbn].borrow_book():
        self.current_loans[isbn] = self.users[library_id]
        self.users[library_id].borrowed_books.append(self.books[isbn])
        print('\33[32m', f"Book {self.books[isbn].get_title()} checked out to {self.users[library_id].name}","\033[0m")
    else:
      print('\33[31m', f"User with id of {library_id} is not a member. Please add this user.", "\033[0m")

   
  def checkin_book(self):
    try:
      isbn = input("Enter the ISBN of the book to return: ")
      library_id = input("What is the users id that wants to return the book? ")
      if isbn in self.books and isbn in self.current_loans and library_id:
        self.books[isbn].return_book()
        self.current_loans.pop(isbn)
        self.users[library_id].borrowed_books.remove(self.books[isbn])
      print(f"Book {self.books[isbn].get_title()} checked in")
    except:
      print('\33[31m', f"Book with ISBN {isbn} is not in the library or has not been checked out.", "\033[0m")
  
  
  def display_borrower_users(self):
    for library_id, user in self.current_loans.items():
      print('\33[33m', {
        library_id: {
          'library_id': user.library_id,
          'name': user.name
        }
      },"\033[0m")
    


  def search_book(self):
    search_criteria = input("Do you want to search based on 'isbn' or 'title'? ")
    if search_criteria == 'isbn':
      isbn = input("Enter the ISBN of the book you are looking for: ")
      found_book = self.books[isbn]
      print("\033[92m",{
                'title': found_book.get_title(),
                'author': found_book.get_author(),
                'ISBN': found_book.get_isbn(),
                'publication_date': found_book.get_publication_date(),
                'is_available': found_book.get_is_available(),
                'genre': found_book.get_genre()
      }, "\033[0m")
      
    elif search_criteria == 'title':
      title = input("Enter the title of the book you are looking for: ")
      for book in self.books.values():
        if book.get_title() == title:
            print("\033[92m",{
                  'title': book.get_title(),
                  'author': book.get_author(),
                  'ISBN': book.get_isbn(),
                  'publication_date': book.get_publication_date(),
                  'is_available': book.get_is_available(),
                  'genre': book.get_genre()
              }, "\033[0m")
       

  def display_genres(self):
    pass
    





  #export data in binary mode and save them inside /data directory
  def export_data(self):
    directory = './data'
    file_path = os.path.join(directory, 'books.txt')
    if not os.path.exists(directory):
        os.makedirs(directory)
   
    
    with open(file_path, 'wb') as file:
        pickle.dump(self.books, file)
        
    with open('data/users.txt', 'wb') as file:   
        pickle.dump(self.users, file)
        
    with open('data/authors.txt', 'wb') as file:   
        pickle.dump(self.authors, file)
        
    with open('data/genres.txt', 'wb') as file:   
        pickle.dump(self.genres, file)
        
    with open('data/current_loans.txt', 'wb') as file:   
        pickle.dump(self.current_loans, file)


  # Import data in binary mode from /data directory  convert it to dictionary 
  def import_data(self):
    with open('data/books.txt', 'rb') as file:
       books_dict = pickle.load(file)
       self.books = books_dict
       
    with open('data/users.txt', 'rb') as file:
       users_dict = pickle.load(file)
       self.users = users_dict  
 
    with open('data/authors.txt', 'rb') as file:
       authors_dict = pickle.load(file)
       self.authors = authors_dict  
     
    with open('data/genres.txt', 'rb') as file:
       genres_dict = pickle.load(file)
       self.genres = genres_dict       

    with open('data/current_loans.txt', 'rb') as file:
       curren_loans_dict = pickle.load(file)
       self.curren_loans = curren_loans_dict  