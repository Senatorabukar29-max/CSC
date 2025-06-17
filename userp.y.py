# Ndubisi Daniel

class Account:
    def __init__(self, name, balance=0):
        self.name = name
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

accounts = {}

def main():
    while True:
        print("\nWelcome to Senator Bank!")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = Account(name)
                print("Account created successfully.")
        elif choice == "2":
            name = input("Enter your name: ")
            if name in accounts:
                account = accounts[name]
                while True:
                    print(f"\nAccount Name: {account.name}\nBalance: {account.balance} naira")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
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
                    elif option == "4":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Account does not exist.")
        elif choice == "3":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
