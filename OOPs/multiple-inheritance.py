class Bank:
    def transaction(self):
        print("Total transaction value")
    def status(self):
        print("Your account is active")
    def deposite(self):
        print("Balance is credited")
    def test(self):
        print("Inside Bank Class")
class HDFC:
    print("You have made successfull transaction to icici from HDFC")
    def test(self):
        print("Inside HDFC Class")
class SBI:
    print("Welcome to SBI Bank")

class icici(Bank,HDFC,SBI):
    pass
# it will give result of test() of Bank class bcoz it has high priority a.k.a MRO(Method Resolution Order)


i = icici()
i.transaction()
i.status()
i.deposite()

i.test() # it will give result of Bank class bcoz it has high priority a.k.a MRO(Method Resolution Order)

'''
How do i execute code which is inside function then print the state of HDFC class
Why it is happening and crux behind of it?
'''