class BankAccount:
    bank_name = "Global Trust Bank"   # CLASS ATTRIBUTE
    total_accounts = 0                # CLASS ATTRIBUTE

    def __init__(self, owner, balance=0):
        self.owner = owner            # INSTANCE ATTRIBUTE
        self._balance = balance       # INSTANCE ATTRIBUTE (protected)
        BankAccount.total_accounts += 1

    # -------- PROPERTY DECORATORS --------
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = value

    # -------- INSTANCE METHODS --------
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}")

    def show_account(self):
        print("\n------ Account Details ------")
        print(f"Bank       : {BankAccount.bank_name}")
        print(f"Owner      : {self.owner}")
        print(f"Balance    : ${self._balance:.2f}")
        print("------------------------------")

    # -------- CLASS METHOD --------
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    # -------- STATIC METHOD --------
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


# Store accounts using a dictionary
accounts = {}


# -------- MENU FUNCTIONS --------
def create_account():
    owner = input("Enter account owner name: ")
    balance = float(input("Initial balance: "))

    acc = BankAccount(owner, balance)
    accounts[owner.lower()] = acc
    print("Account created successfully!")


def access_account():
    name = input("Enter account owner name: ").lower()

    if name not in accounts:
        print("No account found!")
        return

    acc = accounts[name]

    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Account Details")
        print("5. Exit to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            if BankAccount.is_valid_amount(amt):
                acc.deposit(amt)
            else:
                print("Invalid amount!")
        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            if BankAccount.is_valid_amount(amt):
                acc.withdraw(amt)
            else:
                print("Invalid amount!")
        elif choice == "3":
            print(f"Current Balance: ${acc.balance:.2f}")
        elif choice == "4":
            acc.show_account()
        elif choice == "5":
            break
        else:
            print("Invalid option!")


# -------- MAIN MENU LOOP --------
while True:
    print("\n========= Bank Account System =========")
    print("1. Create New Account")
    print("2. Access Existing Account")
    print("3. Total Accounts Created")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        create_account()
    elif option == "2":
        access_account()
    elif option == "3":
        print(f"Total Accounts: {BankAccount.get_total_accounts()}")
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1–4.")
