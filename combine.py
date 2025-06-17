class Account:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Account {self.name} has been credited with {amount} naira. New balance is {self.balance} naira.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount} naira. New balance: {self.balance} naira.")

    def check_balance(self):
        print(f"Current balance: {self.balance} naira.")

class SavingsAccount(Account):
    def __init__(self, name, password, balance=0, interest_rate=0.02):
        super().__init__(name, password, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} naira added. New balance: {self.balance} naira.")

class CurrentAccount(Account):
    def __init__(self, name, password, balance=0, overdraft_limit=1000):
        super().__init__(name, password, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount} naira. New balance: {self.balance} naira.")

accounts = {}

def register_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists.")
        return
    password = input("Set your password: ")
    acc_type = input("Enter account type (regular/savings/current): ").lower()
    if acc_type == "savings":
        accounts[name] = SavingsAccount(name, password)
        print("Savings account created successfully.")
    elif acc_type == "current":
        accounts[name] = CurrentAccount(name, password)
        print("Current account created successfully.")
    else:
        accounts[name] = Account(name, password)
        print("Regular account created successfully.")

def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    account = accounts.get(name)
    if account and account.password == password:
        print("Login successful!")
        return account
    else:
        print("Invalid name or password.")
        return None

def main():
    while True:
        print("\nWelcome to Senator Bank!")
        print("1. Register")
        print("2. Login")
        print("3. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            register_account()
        elif choice == "2":
            account = login()
            if account:
                while True:
                    print(f"\nAccount Name: {account.name}\nBalance: {account.balance} naira")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    if isinstance(account, SavingsAccount):
                        print("4. Add Interest")
                        print("5. Logout")
                    else:
                        print("4. Logout")
                    option = input("Enter your option: ")
                    if option == "1":
                        account.check_balance()
                    elif option == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == "4" and isinstance(account, SavingsAccount):
                        account.add_interest()
                    elif (option == "4" and not isinstance(account, SavingsAccount)) or (option == "5" and isinstance(account, SavingsAccount)):
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == "3":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()