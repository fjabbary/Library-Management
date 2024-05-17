print("Welcome to the Library Management System!")

from library import Library

def main():
    library = Library()

    while True:
        
        print("\n1. Add Book \n2. Display books \n3. Checkout Book \n4. Checkin Book \n5. Add User \n6. Display Users \n7. Display Borrowers \n8. Search Book ")
        choice = input("Enter your choice: ")
        
        try: 
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.display_books() 
            elif choice == "3":
                library.checkout_book()
            elif choice == "4":
                library.checkin_book()
            elif choice == "5":
                library.add_user()
            elif choice == "6":
                library.display_users()        
            elif choice == "7":
                library.display_borrower_users()  
            elif choice == "8":
                library.search_book()    
                
            elif choice == "":
                print("Thanks for supporting your public Library! Have a nice day :)")
                break
            else:
                print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

