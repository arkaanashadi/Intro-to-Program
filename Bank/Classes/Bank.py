from Classes.Customer import *


class Bank(Customer):
    def __init__(self, bank_name, first_name, last_name, balance):
        Customer.__init__(self, first_name, last_name, balance)
        self.bank_name = bank_name

    def addcustomer(self, first_name, last_name, balance):
        self.first_name.append(first_name)
        self.last_name.append(last_name)


    def getcustomer(self, index):
        if not self.first_name:
            return "There are currently no customers"
        else:
            try:
                return """
First name\t: {0}
Last name\t: {1}
{2}
""".format(self.first_name[index], self.last_name[index], self.getbalance(index))
            except:
                return "Sorry, we could not find a customer with that index"

    def getnumofcustomer(self):
        return len(self.first_name)
