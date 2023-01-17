class NavPoint:
    def student(self):
        print("Student details")
class TypeOfClass:
    def student(self):
        print("Type of class")

def external(a):
    a.student()

obj = NavPoint()
obj1 = TypeOfClass()

external(obj)
external(obj1)
print('________________')

def test(a,b):
    return a+b

print(test(4,5))
print(test("Abhinav", "Kumar"))
print(test([1,2,3],[4,5]))