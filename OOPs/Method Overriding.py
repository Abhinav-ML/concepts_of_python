class NavPoint:
    def student(self):
        print("Hey! These are the list of all students")
    def achiever(self):
        print("These students are got placed in 'XYZ' company")
class TnP(NavPoint):
    def student(self):
        print("These students are filtered for interview")

t = TnP()
t.student()
t.achiever()