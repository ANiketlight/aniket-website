class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount


    def log_tran(self, transaction_sting):
        with open("transaction.txt","a")as file:
            file.write( f"{transaction_sting} \t\t\tBalance: {self.balance}\n")


    def withdrawal(self, amount):

        try:

            amount = float(amount)

        except ValueError:
            amount = 0 

        if amount:
            self.balance = self.balance - amount
            self.log_tran(f"withdrew ${amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)

        except ValueError:

            amount = 0  
        if amount:
            self.balance = self.balance + amount
            self.log_tran(f"Deposited ${amount}")
        
account = Bank(50.00)

while True:

    try:
        action = input("what would you like to do withdrawal or deposit ")

    except KeyboardInterrupt:
        print("invalid input ","\n Leaving ATM")
        break


    if action in ["withdrawal","deposit"]:

        if action == "withdrawal":
            amount = input("how much you want to withdrawal : ")
            account.withdrawal(amount)
            print("YOUR BALANCE :",account.balance)

        else:
            amount = input("how much do youwant to deposit in ? ")
            account.deposit(amount)
            print("YOUR BLANCE IS ",account.balance)

    else:
        print("this is invaild syntax")
        
