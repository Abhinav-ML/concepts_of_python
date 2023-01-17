##### importing whole module
# import test2
#
# obj = test2.Person()
# print("check",obj)
# print(obj._name,end=" ")
# print(obj._Person__surname)
# obj1 = test2.Employee()
# print(obj1)
# print(obj1.yob)
# print()
### importing a single from test2 module
# from test2 import Employee

# ## importing module out of directory
# from test import Person
# obj = Person("akk","kk","ak@gmail.com",1994)
# print(obj.name,obj.surname,obj.emailid,obj.year_of_birth)

##### importing from other directory a.k.a Package
from util.utils1 import Person


class Person1:
    def __init__(self, name, surname, yob):
        self.name1 = name  # public variable
        self._surname1 = surname  # protected variable
        self.__yob = yob  # private variable


sudh = Person1('Sudhansu', 'Kumar', 1994)
print("******")
print(sudh.name1)  # calling public variable
print(sudh._surname1)  # calling protected variable
print(sudh._Person1__yob)  # calling private variable
