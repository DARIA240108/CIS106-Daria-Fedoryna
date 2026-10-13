# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:00:06 2026

@author: daria
"""

#Book tracker - final project
#This program help users organize their books. 
#They can add, delete, view and find books.
#Program saves books to a file, so users can store their book without worrying
#that they will get lost.

books = []
#Main function of the program that runs users choices 
def main():
    loadBooks()
    while True:
        choice = menu()
        if choice == "5":
            break
        elif choice == "1":
            addBooks()
            saveBooks()
            print()
        elif choice == "2":
           viewBooks()
           print()
        elif choice == "3":
            findBooks()
            print()
        elif choice == "4":
            deleteBooks()
            saveBooks()
            print()
        else: 
            print("Opps, wrong choice. Please try again!")
        
  #User can add a new book to the list      
def addBooks():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    book = {"title": title, "author": author, "genre": genre}
    books.append(book)
    print()
    print("Book added successfully")
    
#User can view books that they added to the list, if there is nothing
#in the list, message will be displayed
def viewBooks():
    if not books:
        print("No books found")
    else: 
        for book in books:
            print(book["title"], "-", book["author"], "-", book["genre"])

#user can find any book that they added to the list by book title
def findBooks():
    print()
    title = input("Enter book title to find a book: ")
    for book in books: 
        if book["title"].lower() == title.lower():
            print(book["title"], "-", book["author"], "-", book["genre"])
            return
        print("Sorry, book not found!")
 
#User can delete book from the list
def deleteBooks():
    title = input("Enter book title to delete: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Sorry, book not found!")

#Function saves all books to a text file
def saveBooks():
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book["title"] + "," + book["author"] + "," + book["genre"] + "\n")

#Function loads saved books from a text file
def loadBooks():
    try:
        with open("books.txt", "r") as file:
            for line in file:
                title, author, genre = line.strip().split(",")
                book = {"title": title, "author": author, "genre": genre}
                books.append(book)
    except FileNotFoundError:
        pass
                
 #Function displays menu and gets user choice, then send everything to the 
#main function  
def menu():
    print("Welcome to book tracker!")
    print("Please choose one of the following: ")
    print()
    print("1. Add a book")
    print("2. View Books")
    print("3. Find a book ")
    print("4. Delete a book")
    print("5. Quit")
    choice = input("Select your choice: ")
    return choice

main()
