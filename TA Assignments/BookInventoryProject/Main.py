from Classes.Book import *
from Classes.People import *

inventory = Book("bob", 100, 1, ["tom"], ["@tom"])

managers = Manager(["bob"],  # Name
                   ["@bob"],  # Email
                   [100],  # Wage
                   ["1"],  # ID
                   [[]])  # Supervising

employees = Employee([],  # Name
                     [],  # Email
                     [],  # Wage
                     [])  # ID


def dialogues(request):
    if request == "employee actions":
        return """What would you like to do?
[Info]
[Find Book]
[Display Books]
[Add Book]
[Logout]
"""
    elif request == "manager actions":
        return """
Manager actions:
[Add Employee]
[Add Manager]
[Supervise New Employee]
"""


def actions(user, id_number, position):

    # To obtain index
    index = 0
    for id_num in position.getidnumbers():
        if id_num == id_number:
            break
        index += 1

    if user == "info":
        print("\n{0}\n".format(position.getinfo(index)))

    elif user == "find book":
        if len(inventory.listbooks().split(" ")) == 0:
            print("No books in inventory yet\n")
        else:
            print(inventory.findbook(input("Please input book title ").title()))

    elif user == "display books":
        print("\nBooks available: "
              "\n{0}\n".format(inventory.listbooks().title()))

    elif user == "add book":
        inventory.addbook()

    elif user == "logout":
        main(1, 1, 0)

    if id_number in managers.getidnumbers():
        manageractions(user, id_number, position, index)

    else:
        print("Invalid input")

    main(1, 2, id_number)


def manageractions(user, id_number, position, index):
    if user == "add employee":
        x = 1
        while x == 1:
            name = input("Input new employee's name ")
            email = input("Input new employee's email ")
            while True:
                try:
                    wage = float(input("Input new employee's wage "))
                    break
                except:
                    print("Invalid input")
            while True:
                id_num = input("Input new employee's ID ")

                if (id_num in employees.getidnumbers()) or (id_num in managers.getidnumbers()):
                    print("That ID has been taken")

                else:
                    break
            print("""
Name: {0}
Email: {1}
Wage: {2}
ID: {3}""".format(name.title(), email, wage, id_num))
            while True:
                user = input("is the information above correct? \n[Yes]\n[No]\n").lower()
                if user == "no":
                    break
                elif user == "yes":
                    x = 0
                    break
                else:
                    print("Invalid input")

        employees.addemployee(name, email, wage, id_num)

    elif user == "add manager":
        if len(employees.name) == 0:
            print("There are no employees yet")
            main(1, 2, id_number)
        z = 1
        while z == 1:
            name = input("Input new manager's name ")
            email = input("Input new manager's email ")
            while True:
                try:
                    wage = float(input("Input new manager's wage "))
                    break
                except:
                    print("Invalid input")
            while True:
                id_num = input("Input new manager's ID ")

                if (id_num in employees.getidnumbers()) or (id_num in managers.getidnumbers()):
                    print("That ID has been taken")

                else:
                    break
            supervising = []
            x = 1
            while x == 1:
                inp = input("Please input employee name ").lower()

                if inp in employees.name:
                    supervising.append(inp)
                else:
                    print("Employee not found")
                    continue

                while True:
                    user = input("Would you like to add another employee?\n[Yes]\n[No]\n").lower()
                    if user == "yes":
                        break
                    elif user == "no":
                        x = 0
                        break
                    else:
                        print("Invalid input")
            print("""
Name: {0}
Email: {1}
Wage: {2}
ID: {3}
Supervising: {4}""".format(name.title(), email, wage, id_num, ", ".join(supervising).title()))
            while True:
                user = input("is the information above correct? \n[Yes]\n[No]\n").lower()
                if user == "no":
                    break
                elif user == "yes":
                    z = 0
                    break
                else:
                    print("Invalid input")
        managers.addmanager(name, email, wage, id_number, supervising)

    elif user == "supervise new employee":
        if len(employees.name) == 0:
            print("There are no employees yet")
            main(1, 2, id_number)
        x = 1
        while x == 1:
            inp = input("Please input employee name ").lower()

            if inp in employees.name:
                managers.addsupervising(index, inp)
            else:
                print("Employee not found")
                continue

            while True:
                user = input("Would you like to add another employee?\n[Yes]\n[No]\n").lower()
                if user == "yes":
                    break
                elif user == "no":
                    x = 0
                    break
                else:
                    print("Invalid input")


def main(runs, phase, id_number):

    # Initial run, sets the first manager
    if runs == 0:
        print("You are now a manager of a bookstore")
        name = input("Please input your name ")
        email = input("Please input yout email ")

        while True:
            try:
                wage = float(input("Please set your wage "))
                break

            except:
                print("Invalid input")

        id_number = "1"
        supervising = []
        managers.addmanager(name, email, wage, id_number, supervising)
        phase = 1
        
    elif (runs == 1) and (phase == 1):
        id_number = input("Please input your ID number ")
        phase = 2

    if (runs == 1) and (phase == 2):
        if id_number in managers.getidnumbers():
            user = input(dialogues("employee actions")+dialogues("manager actions")).lower()
            actions(user, id_number, managers)

        elif id_number in employees.getidnumbers():

            user = input(dialogues("employee actions")).lower()
            actions(user, id_number, employees)

        else:
            print("invalid ID")
            main(1, 1, 0)

main(0, 0, 0)
