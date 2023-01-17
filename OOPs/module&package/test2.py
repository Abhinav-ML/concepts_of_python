# import test1
#
# print(test1)
#
# obj3 = test1.Person1("Virat","Kohli",1990)
# print(obj3)
# print(obj3.name1,obj3._surname1,",YOB:",obj3._Person1__yob)
# print()
class Person:

    _name = "Abhinav"
    __surname = "Kumar"
    yob = 1998

    def _age(self,current_year): # creating protected method
        return current_year - self.yob
    def __age1(self,current_year): # creating private method
        return current_year - self.yob

class Employee(Person):
    yob = 1997

print("#########")
obj = Person()
obj1 = Employee()
print(obj)
print(obj._name)
print(obj._Person__surname)
print(obj.yob)
print("*****")

print(obj._age(2022))
print(obj._Person__age1(2022))

print("****")
print(obj1.yob)
print(obj1._name)
print(obj1._Person__surname)
print("*****")

print(obj1._age(2022))
print(obj1._Person__age1(2022))

print("****")