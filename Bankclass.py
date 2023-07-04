class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance =balance

    def deposit(self,amount):
        self.balance +=amount

    def withdrawal(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account number: {self.account_number}")
        print(f"Holder name : {self.holder_name}")
        print(f"Balance: {self.balance}")

my_account=BankAccount("123456789", "Erick", 1000)
my_account.display_balance()
my_account.deposit(500)
my_account.display_balance()
my_account.withdrawal(200)
my_account.display_balance()
my_account.withdrawal(2000)
my_account.display_balance()


