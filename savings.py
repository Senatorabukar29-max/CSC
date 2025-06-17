#Princess Emmanuel Okhai

class SavingsAccount:
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} naira added. New balance: {self.balance} naira.")
