class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = Person("Muskan","bhandari","muskan@gmail.com",2002)
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)