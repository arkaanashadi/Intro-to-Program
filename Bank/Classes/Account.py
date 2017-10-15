class Account:

    def __init__(self, balance):
        self.__balance = balance

    def getbalance(self, index):
        return "Balance\t\t: {0}".format(self.__balance[index])

    def addbalance(self, amt):
        self.__balance.append(amt)

    def deposit(self, amt, index):
        self.__balance[index] += amt
        return "Your current balance is now {0}\n".format(self.__balance[index])

    def withdraw(self, amt, index):
        if amt > self.__balance[index]:
            return "insufficient balance"
        elif amt <= self.__balance[index]:
            self.__balance[index] -= amt
            return """{0} have been withdrawn from your account
{1} remaining in your balance""".format(amt, self.__balance[index])
