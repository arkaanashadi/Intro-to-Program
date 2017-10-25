from Classes.People import *

class Book(Person):
    def __init__(self, book_name, price, quantity, name, email):
        Person.__init__(self, name, email)
        self.book = {book_name: [price, quantity, name, email]}

    # To add a new book
    def addbook(self):
        z = 1
        while z == 1:
            book_name = input("Please input book name ")
            while True:
                try:
                    price = float(input("Please input book price "))
                    break
                except:
                    print("Invalid input")
            while True:
                try:
                    quantity = int(input("Please input book quantity "))
                    break
                except:
                    print("Invalid input")
            authors = []
            emails = []
            x = 1
            while x == 1:
                authors.append(input("Please input author name ").lower())
                emails.append(input("Please input author email ").lower())
                while True:
                    user = input("Would you like to add another author?\n[Yes]\n[No]\n").lower()
                    if user == "yes":
                        break
                    elif user == "no":
                        x = 0
                        break
                    else:
                        print("Invalid input")
            print("""Name: {0}
Price: {1}
Quantity: {2}
Authors: {3}
emails: {4}""".format(book_name.title(), price, quantity, ", ".join(authors), ", ".join(emails)))
            user = input("is the information above correct? \n[Yes]\n[No]\n").lower()
            while True:
                if user == "no":
                    break
                elif user == "yes":
                    z = 0
                    break
                else:
                    print("Invalid input")

        self.book[book_name] = [price, quantity, authors, emails]

    # Find book and print info
    def findbook(self, book_name):
        if book_name.lower() in self.book.keys():
            for book, items in self.book.items():
                if book.lower() == book_name.lower():
                    price = items[0]
                    quantity = items[1]
                    name = ", ".join(items[2])
                    email = ", ".join(items[3])
                    return """
Book name: {0}
Author(s): {1}
Email(s): {2}
price: {3}
Quantity: {4}
""".format(book_name.title(), name.title(), email, price, quantity)

        else:
            return "Sorry we could not find that book\n"

    # To list all books in inventory
    def listbooks(self):
        return "\n".join(self.book.keys())
