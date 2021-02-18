import datetime
class Bank:
    bank="SBI"

    def create_account(self,acc_no,c_name,ph_no,bal):

        self.acc_no=acc_no
        self.c_name=c_name
        self.ph_no=ph_no
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print(Bank.bank,"Account number:",self.acc_no,"is be creditied",amount,"on",datetime.datetime.now(),"you aval bal:",self.bal)

    def withdraw(self,amount):
        if amount>self.bal:
            print("transaction failed ")
        else:
            self.bal-=amount
            print("Account number:", self.acc_no, "is be debitied", amount,"your aval bal",self.bal)


    def balance(self):
        print("YOUR AVAIBLE BALANCE IS ",self.bal)


    def details(self):
        print("ACCOUNT NO:",self.acc_no)
        print("CUSTOMER NAME:",self.c_name)
        print("PHONE NO.:",self.ph_no)
        print("GRAND TOTAL AMOUNT: ",self.bal)


obj=Bank()
obj.create_account(101,'bibin',9897968907,50000)
obj.details()
obj.withdraw(2000)
obj.deposit(44000)
