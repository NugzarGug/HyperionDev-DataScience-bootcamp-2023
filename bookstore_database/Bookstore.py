import sqlite3
from prettytable import PrettyTable
# creates database and table books
ebookstore_db = sqlite3.connect('ebookstore')
cursor = ebookstore_db.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS 
               books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
               ''')
# defines variables which contains information about books
id1, id2, id3, id4, id5, = 3001, 3002, 3003, 3004, 3005
title1, title2, title3, title4, title5 = ('A Tale of Two Cities',
                                          "Harry Potter snd the Philosopher's Stone",
                                          'The Lion, the Witch and the Wardrobe',
                                          'The lord of the Rings',
                                          'Alice in Wonderland')
author1, author2, author3, author4, author5 = ('Charles Dickens',
                                               'J.K. Rowling',
                                               'C.S. Lewis',
                                               'J.R.R Tolkien',
                                               'Lewis Carroll')
qty1, qty2, qty3, qty4, qty5 = 30, 40, 25, 37, 12
books_data = [(id1,title1,author1,qty1),
              (id2,title2,author2,qty2),
              (id3,title3,author3,qty3),
              (id4,title4,author4,qty4),
              (id5,title5,author5,qty5)]
# checking table books anв if it is empty adds 5 books into the table
cursor.execute(''' SELECT COUNT(*) FROM books''')
count = cursor.fetchone()[0]
if count == 0:
    cursor.executemany(''' INSERT INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)
               ''', books_data)
        
# creates class book, which can create an object book with id, title, author, and quantity
class Book():
    def __init__ (self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
    def get_id(self):
        return self.id    
    def get_title(self):
        return self.title    
    def get_author(self):
        return self.author
    def get_quantity(self):
        return self.quantity
    @classmethod
    def create_book(cls):
        id = int(input('Plese enter id: '))
        title = input('Please enter the title of the book: ')
        author = input('Please enter the author of the book: ')
        quantity = int(input('Please enter the quantity of the book: '))
        return cls(id, title, author, quantity)
# defines search function, which can search book in database and display results
# where search object where we will search in the table column (Title, Author or id)
# search_input - what we will search 
def search(search_object,search_input):
    if search_object == 'Title':
        querry = ('''SELECT * FROM books WHERE Title = ?''')
    elif search_object == 'id':
        querry = ('''SELECT * FROM books WHERE id = ?''')
    elif search_object == 'Author':
        querry = ('''SELECT * FROM books WHERE Author = ?''') 
    else:
        print(f'Invalid search object: {search_object}')
        
    cursor.execute(querry,(search_input,))
    results = cursor.fetchall()
    if len(results) == 0:
        print('Nothing was found\n')
        return False
# displays results of the searching
    else:
        table = PrettyTable()
        table.field_names = ['ID', 'Title', 'Name', 'Qty']
        for i in results:
                table.add_row(i)
        print(table, '\n')
        return True
        
# defines function, which displays the main menu                
def main_menu():
    print('Enter "A" for add book to the database')
    print('Enter "U" to update book information')
    print('Enter "D" to delete book from database')
    print('Enter "S" to search in the database')
    print('Press "Q" for quit programm\n')
# defines function which displays update mebu
def update_menu():
    print('What do you want to update ?')
    print('Enter "1" for ID')
    print('Enter "2" for Title')
    print('Enter "3" for Name')
    print('Enter "4" for Qty\n')
# displays main menu and waits user entry
choice_done = False
while choice_done == False:
    main_menu()
    user_choice = input('Please enter your choice: ').upper()
# adds books to the database
    if user_choice == 'A':
        book = Book.create_book()
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)
                       ''',(book.id, book.title, book.author, book.quantity))
        ebookstore_db.commit()
        print('The book has successfully added !\n')
# search book in the database
    if user_choice == 'S':       
        while True:
            try:
                print('\nPlease choose your search criteria:\n'
                      '1 for ID\n'
                      '2 for Title\n'
                      '3 for Author\n')
                search_choice = int(input('Please enter: '))
                if search_choice not in [1, 2, 3]:
                    print("Oops! That was an incorrect entry. Try again...")
                    continue
            except ValueError:
                print("Oops! That was an incorrect entry. Try again...")
                continue       
            
            if search_choice in [1, 2, 3]:
                if search_choice == 1:
                    search_object = 'id'
                    search_input = input('Please enter the id: ')
                elif search_choice == 2:
                    search_object = 'Title'
                    search_input = input('Please enter the name of the book: ')
                elif search_choice == 3:
                    search_object = 'Author'
                    search_input = input('Please enter the author of the book: ')
                search(search_object, search_input)
                break
             
# allows update records in the database    
    if user_choice == 'U':
        while True:
            try:
                search_object = 'id'
                update_id = int(input('\nPlease enter the id of the book you want to update: '))
                if search(search_object,update_id) == False:
                    choice_done = False
                    break
            
                else:
                    choice_done = True
                    update_menu()
                    update_choice = int(input('Please enter your choice: '))
                    if update_choice in [1, 2, 3, 4]:
# updates id of the book
                        if update_choice == 1:
                            while True:
                                try:
                                    choice_id = int(input('Please enter new ID: '))
                                    break
                                except Exception:
                                    print("Oops! That was incorrect enter. Try again...")
                            cursor.execute('''UPDATE books SET id = ? WHERE id = ?''',(choice_id,update_id))
                            ebookstore_db.commit()
                            print('Changes successfully saved\n')
                            choice_done = False
                            break
# updates the name of the book
                        elif update_choice == 2:
                            update_title = input('Please enter the new name of the book: ')
                            cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''',(update_title,update_id))
                            ebookstore_db.commit()
                            print('Changes successfully saved\n')
                            choice_done = False
                            break
# updates author of the book
                        elif update_choice == 3:
                            update_author = input('Please enter the new author: ')
                            cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''',(update_author,update_id))
                            ebookstore_db.commit()
                            print('Changes successfully saved\n')
                            choice_done = False
                            break
# updates quantity of the book
                        elif update_choice == 4:
                            while True:
                                try:
                                    update_quantity = int(input('Please enter the new quantity: '))
                                    break
                                except Exception:
                                    print("Oops! That was incorrect enter. Try again...")
                            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''',(update_quantity,update_id))
                            ebookstore_db.commit()
                            print('Changes successfully saved\n')
                            choice_done = False
                            break
            except Exception:
                print("Oops! That was incorrect enter. Try again...")
# allows the user to delete the book       
    if user_choice == 'D':
        while True:
            try:
                ask_id = int(input('Please enter the id of the book you want to delete: '))
                break
            except Exception:
                print("Oops! That was incorrect enter. Try again...")               
        cursor.execute('''DELETE FROM books WHERE id = ?''', (ask_id,))
        if cursor.rowcount == 0:
            print(f"Book with id {ask_id} not found in the table")
        else:
            print(f"Book with id {ask_id} has been successfully deleted")
 # quit the programme           
    if user_choice == 'Q':
        quit()
