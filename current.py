#Embaga Ashur

class CurrentAccount:
    def __init__(self, name, balance=0, overdraft_limit=1000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount} naira. New balance: {self.balance} naira.")
