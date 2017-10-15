from Classes.Bank import *


def action(bank, index):

    print("What would you like to do Mr./Ms. {0}?".format(bank.getlastname(index)))

    while True:
        print("[Deposit]\n[Withdraw]\n[Logout]\n[Info]")

        user = input()

        if user == "deposit":
            while True:
                try:
                    dep = float(input("\nHow much would you like to deposit?\n"))
                    break
                except:
                    print("Invalid input")
            print(bank.deposit(dep, index))

        elif user == "withdraw":
            while True:
                try:
                    wit = float(input("\nHow much would you like to withdraw?\n"))
                    break
                except:
                    print("Invalid input")
            print(bank.withdraw(wit, index))

        elif user == "info":
            print(bank.getcustomer(index))

        elif user == "logout":
            print("Thank you for choosing our bank")
            break

        else:
            print("Invalid input")
            action(bank, index)


def dialogues(request):

    # Account input error
    if request == "account_input_error":
        return ("""
We could not find your account
please make sure your first name and last name 
are typed in correctly
""")

    # Login or New account
    elif request == "LogOrNew":
        return """would you like to login to your account 
or make a new account?
[Login]
[New account]
"""


def main(runs, bank):

    # for initial run of program (to input bank name)
    if runs == 0:
        bank = Bank(
                input("Please give the bank a name "),  # Bank Name
                [],  # First name
                [],  # Last name
                []  # Balance
            )
        main(1, bank)

    elif runs == 1:

        user = input("\nWelcome to the {0} bank\n{1}".format(bank.bank_name, dialogues("LogOrNew"))).lower()

        while True:

            # Catch login attempt with no accounts yet
            if user == "login" and bank.getnumofcustomer() <= 0:
                print("There are no existing accounts yet")
                main(1, bank)

            # Login
            elif user == "login" and bank.getnumofcustomer() > 0:

                while True:

                    first_name = input("Please input your first name ")
                    last_name = input("Please input your last name ")

                    if first_name in bank.first_name and last_name in bank.last_name:
                        break

                    else:
                        print(dialogues("account_input_error"))

                first_count = 0
                for first in bank.first_name:

                    if first == first_name:
                        break
                    else:
                        first_count += 1

                last_count = 0
                for last in bank.last_name:

                    if last == last_name:
                        break
                    else:
                        last_count += 1

                if first_count == last_count:
                    index = int(last_count)

                else:
                    print(dialogues("account_input_error"))
                    continue

                print(bank.getcustomer(index))

                action(bank, index)
                main(1, bank)

            # New account
            elif user == "new account":
                x = 1
                while x == 1:
                    first_name = input("What is your first name? ").title()
                    last_name = input("What is yout last name? ").title()

                    if first_name in bank.first_name and last_name in bank.last_name:
                        print("Account already exist")
                        main(1, bank)

                    while True:
                        user = input("is the information above correct? \n[Yes]\n[No]\n").lower()

                        if user == "no":
                            break

                        elif user == "yes":
                            x = 0
                            break

                        else:
                            print("Invalid input")

                while True:
                    try:
                        amt = float(input("\nPlease input a starting deposit "))
                        break
                    except:
                        print("Invalid input")

                bank.first_name.append(first_name)
                bank.last_name.append(last_name)
                bank.addbalance(amt)

                print(bank.getcustomer(-1))

                action(bank, -1)

                main(1, bank)

            # Input validator
            else:
                print("Invalid input")
                user = input(dialogues("LogOrNew"))

main(0, "")
