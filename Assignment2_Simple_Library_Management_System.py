Simple_Library_management_system:

Stored_books = {"Python Basic", "Data Science 101", "AI for Beginners" }
print(Stored_books)

def view_books():
    if Stored_books:
        print('\nThese are the books I currently have:\n')
        for idx, Stored_books in enumerate (Stored_books, start = 1):
            print(f'{idx}, {Stored_books}')

    else:
        print('no books are currently available')

def borrow_stored_books():
    if not Stored_books:
        print('\nThere are no books available to borrow at the moment.')
        return
    
    view_stored_books(): 
    if Stored_books:
        Stored_books_name = input('\Enter the name of the book you want to borrow. ')
        if Stored_books_name in Stored_books:
            Stored_books.remove(Stored_books_name)
            print(f'\nYou have borrowed "(stored_book_name)". ')
        else: 
            print('The book is not available')

    def return_stored_books():
        while True:
            print("\nWhat do you want to do at my library?\n")
            print("1. veiw teh books I have available")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Leave the library")

            choice = input('\nEnter your choice (pick any number from 1-4): ')

            if choice == '1':
                view_stored_books()

            elif choice == '2':
                borrow_stored_books
            elif choice == '3':
                return_stored_books
            elif choice == '4':
                Leave_the_library
            
            else:
                print("nInvalid Choice. Please select numbers 1 to 4.")
    except ValueError:
        print("\nInvalid input. Please entera  number")