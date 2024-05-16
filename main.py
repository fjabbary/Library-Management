

from library import Library

def main():
    library = Library()

    while True:
        print("Welcome to the Library Management System!")
        print("\n1. Add Book \n2. Checkout book \n3. Return Book \n4. Exit")
        choice = input("Enter your choice: ")
        
        try: 
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.checkout_book()
            elif choice == "3":
                library.checkin_book()
            elif choice == "4":
                library.display_books()    
            elif choice == "":
                print("Thanks for supporting your public Library! Have a nice day :)")
                break
            else:
                print("Please enter a valid choice")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

