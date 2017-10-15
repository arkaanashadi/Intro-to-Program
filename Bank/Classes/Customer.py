from Bank.Classes.Account import *


class Customer(Account):

    def __init__(self, first_name, last_name, balance):
        Account.__init__(self, balance)
        self.first_name = first_name
        self.last_name = last_name
        # self.id

    def getfirstname(self, index):
        return self.first_name[index]

    def getlastname(self, index):
        return self.last_name[index]

    def getaccount(self, index):
        return self.getbalance(index)
