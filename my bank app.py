#David Ezra

import streamlit as st

# In-memory storage for accounts
accounts = {}

class Account:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Successfully withdrew {amount} naira. New balance: {self.balance} naira."

    def check_balance(self):
        return f"Current balance: {self.balance} naira."

class SavingsAccount(Account):
    def __init__(self, name, password, balance=0, interest_rate=0.02):
        super().__init__(name, password, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of {interest} naira added. New balance: {self.balance} naira."

class CurrentAccount(Account):
    def __init__(self, name, password, balance=0, overdraft_limit=1000):
        super().__init__(name, password, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Withdrawal exceeds overdraft limit."
        else:
            self.balance -= amount
            return f"Successfully withdrew {amount} naira. New balance: {self.balance} naira."

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.account_name = ""
    st.session_state.account_type = ""
    st.session_state.account = None

st.title("Senator Bank")

if not st.session_state.logged_in:
    st.header("Register or Login")

    tab1, tab2 = st.tabs(["Register", "Login"])

    with tab1:
        reg_name = st.text_input("Name", key="reg_name")
        reg_pass = st.text_input("Password", type="password", key="reg_pass")
        reg_type = st.selectbox("Account Type", ["Regular", "Savings", "Current"], key="reg_type")
        if st.button("Register"):
            if reg_name in accounts:
                st.error("Account already exists.")
            elif not reg_name or not reg_pass:
                st.error("Please enter a name and password.")
            else:
                if reg_type == "Savings":
                    accounts[reg_name] = SavingsAccount(reg_name, reg_pass)
                elif reg_type == "Current":
                    accounts[reg_name] = CurrentAccount(reg_name, reg_pass)
                else:
                    accounts[reg_name] = Account(reg_name, reg_pass)
                st.success(f"{reg_type} account created successfully.")

    with tab2:
        log_name = st.text_input("Name", key="log_name")
        log_pass = st.text_input("Password", type="password", key="log_pass")
        if st.button("Login"):
            account = accounts.get(log_name)
            if account and account.password == log_pass:
                st.session_state.logged_in = True
                st.session_state.account_name = log_name
                st.session_state.account = account
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid name or password.")

else:
    account = st.session_state.account
    st.header(f"Welcome, {account.name}!")
    st.write(account.check_balance())

    if isinstance(account, SavingsAccount):
        options = ["Check Balance", "Deposit", "Withdraw", "Add Interest", "Logout"]
    else:
        options = ["Check Balance", "Deposit", "Withdraw", "Logout"]

    choice = st.selectbox("Choose an action", options)

    if choice == "Check Balance":
        st.info(account.check_balance())

    elif choice == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=0.0, step=1.0)
        if st.button("Deposit"):
            account.deposit(amount)
            st.success(f"Deposited {amount} naira. New balance: {account.balance} naira.")

    elif choice == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=1.0)
        if st.button("Withdraw"):
            msg = account.withdraw(amount)
            if "Successfully" in msg:
                st.success(msg)
            else:
                st.error(msg)

    elif choice == "Add Interest" and isinstance(account, SavingsAccount):
        if st.button("Add Interest"):
            msg = account.add_interest()
            st.success(msg)

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.account_name = ""
        st.session_state.account = None
        st.success("Logged out successfully.")
        st.experimental_rerun()
        
