''' Examples of
Conflicts will arise here bcoz of data members and method members name are same .
'''
# class NavPoint:
#     def __init__(self):
#         self.students = "Data Science"
#
#     def students(self):
#         print(self.students)
# obj = NavPoint()
# obj.students()

#### Now removing conflicts
class NavPoint:
    def __init__(self):
        self.domain = "Data Science"

    def students(self):
        print(self.domain)
obj = NavPoint()
obj.students()
obj.domain = 'BigData' #trying to override the value of variable in a run-tume
obj.students()
print("________________________")
class NavPoint1:
    def __init__(self):
        self.__domain = "Data Science"

    def students(self):
        print(self.__domain)
    def students_change(self):
        self.__domain = "Data Analytics"
        print(self.__domain)

obj2 = NavPoint1()
obj2.students()
obj2.__domain = 'BigData' #trying to override the value of PRIVATE variable in a run-tume it wiil not override, value will be same.(infact It will not give error)
obj2.students()

'''#this time it will override the value of PRIVATE variable as we are doing via method'''
obj2.students_change()

print("_____________________")

'''some changes in above code'''
class NavPoint1:
    def __init__(self):
        self.__domain = "Data Science"

    def students(self):
        print(self.__domain)
    def students_change(self,update):
        self.__domain = update
        print(self.__domain)

obj2 = NavPoint1()

obj2.students_change('Machine Learning Engineer') #this time it will override the value of PRIVATE variable in run-time as we are doing via method.

