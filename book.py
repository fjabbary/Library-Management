class Book():
  def __init__(self, title, author, ISBN, publication_date):
    self.__title = title
    self.__author = author
    self.__ISBN = ISBN
    self.__publication_date = publication_date
    self.__is_available = True
    
  def get_title(self):
    return self.__title
  
  def get_author(self):
    return self.__author
  
  def get_isbn(self):
    return self.__ISBN
  
  def get_publication_date(self):
    return self.__publication_date
  
  def get_is_available(self):
    return self.__is_available
  
  def set_is_available(self, is_available):
    self.__is_available = is_available
    
  def borrow_book(self):
    if self.get_is_available():
      self.set_is_available(False)
      
      return True
    return False
  
  def return_book(self):
      self.set_is_available(True)
        
        
class FictionBook(Book):
  def __init__(self, title, author, ISBN, publication_date, sub_genre):        
        super().__init__(title, author, ISBN, publication_date)
        self.__genre = 'Fiction'
        self.__sub_genre = sub_genre
        
  def get_genre(self):
    return self.__genre
  
  def get_sub_genre(self):
    return self.__sub_genre
        
        
class NonFictionBook(Book):
  def __init__(self, title, author, ISBN, publication_date, sub_genre):        
        super().__init__(title, author, ISBN, publication_date)
        self.__genre = 'Non-Fiction'
        self.__sub_genre = sub_genre
          
  def get_genre(self):
    return self.__genre
  
  def get_sub_genre(self):
    return self.__sub_genre