class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Employee(Person):
    def __init__(self, name, email, wage, id_number):
        Person.__init__(self, name, email)
        self._wage = wage
        self._id_number = id_number

    def getwage(self, index):
        return self._wage[index]

    def getidnumbers(self):
        return self._id_number

    def getinfo(self, index):
        return """Name: {0}
Email: {1}
Wage: {2}
ID: {3}""".format(self.name[index].title(),
                  self.email[index],
                  self._wage[index],
                  self._id_number[index])

    def addemployee(self, name, email, wage, id_number):
        self.name.append(name)
        self.email.append(email)
        self._wage.append(wage)
        self._id_number.append(id_number)


class Manager(Employee):
    def __init__(self, name, email, wage, id_number, supervising):
        Employee.__init__(self, name, email, wage, id_number)
        self.supervising = supervising

    def getinfo(self, index):

        return """Name: {0}
Email: {1}
Wage: {2}
ID: {3}
Supervising: {4}""".format(self.name[index],
                           self.email[index],
                           self._wage[index],
                           self._id_number[index],
                           ", ".join(self.supervising[index]).title())

    def addsupervising(self, index, employee):
        self.supervising[index].append(employee)

    def addmanager(self, name, email, wage, id_number, supervising):
        self.name.append(name)
        self.email.append(email)
        self._wage.append(wage)
        self._id_number.append(id_number)
        self.supervising.append(supervising)
