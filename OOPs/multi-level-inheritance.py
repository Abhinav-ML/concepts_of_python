class Bank:
    def transaction(self):
        print("Total transaction value")
    def status(self):
        print("Your account is active")
    def deposite(self):
        print("Balance is credited")
class HDFC(Bank):
    print("You have made successfull transaction to icici from HDFC")
class icici(HDFC):
    pass

i = icici()
# print(i.transaction()) ## this will give you None in output as well
# bcoz we are not returning any thing in function
# print(i.status())
# print(i.deposite())
i.transaction()
i.status()
i.deposite()