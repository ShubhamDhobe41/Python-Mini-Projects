from abc import ABC, abstractmethod

# -------------------------------
# 1️⃣ Abstraction
# -------------------------------
class Account(ABC):
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self._balance = balance   # protected
        self.transactions = []

    @abstractmethod
    def account_type(self):
        pass

    def show_details(self):
        print(f"Name: {self.name}, Account No: {self.acc_no}, Balance: {self._balance}")


# -------------------------------
# 2️⃣ Encapsulation + Inheritance
# -------------------------------
class SavingsAccount(Account):

    def account_type(self):
        return "Savings Account"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Deposit Successful")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")


# -------------------------------
# 3️⃣ Another Child Class
# -------------------------------
class CurrentAccount(Account):

    def account_type(self):
        return "Current Account"

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount <= self._balance + 5000:  # overdraft
            self._balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal Successful (Overdraft Allowed)")
        else:
            print("Limit Exceeded")


# -------------------------------
# 4️⃣ Composition
# -------------------------------
class Bank:
    def __init__(self):
        self.accounts = []   # Bank HAS-A accounts

    def add_account(self, acc):
        self.accounts.append(acc)

    def show_all_accounts(self):
        for acc in self.accounts:
            acc.show_details()


# -------------------------------
# 5️⃣ Polymorphism in Action
# -------------------------------
bank = Bank()

acc1 = SavingsAccount("Vaibhav", 101, 1000)
acc2 = CurrentAccount("Rahul", 102, 2000)

bank.add_account(acc1)
bank.add_account(acc2)

# Perform operations
acc1.deposit(500)
acc1.withdraw(200)

acc2.deposit(1000)
acc2.withdraw(6000)

# Show all accounts
print("\n--- All Accounts ---")
bank.show_all_accounts()

# Transaction history
print("\n--- Transactions ---")
for t in acc1.transactions:
    print("Vaibhav:", t)

for t in acc2.transactions:
    print("Rahul:", t)