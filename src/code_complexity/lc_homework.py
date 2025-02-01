class Account:
    def __init__(
        self,
        customer_id: int,
        account_number: int,
        balance: float
    ):
        self.account_number = account_number
        self.customer_id = customer_id
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0.0:
            self.balance += amount
        else:
            raise ValueError("Cannot deposit negative amount")

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

class Customer:
    def __init__(
        self,
        id: int,
        name: str,
        address: str
    ):
        self.id = id
        self.name = name
        self.address = address

class Bank:
    def __init__(self):
        self.__account_counter = 0
        self.__customer_counter = 0
        self.accounts = {}
        self.customers = {}

    def become_customer(
        self,
        name: str,
        address: str
    ) -> Customer:
        customer = Customer(self.__customer_counter, name, address)
        self.customers[self.__customer_counter] = customer
        self.__customer_counter += 1
        return customer

    def create_account(
        self,
        customer_id: int,
        initial_balance: float
    ) -> Account:
        account = Account(customer_id, self.__account_counter, initial_balance)
        self.accounts[self.__account_counter] = account
        self.__account_counter += 1
        return account

    def get_account(
        self,
        account_number: int
    ) -> Account:
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def get_customer(
        self,
        customer_id: int
    ) -> Customer:
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            raise ValueError("Customer not found")

def banking_scenario():
    bank = Bank()

    customer1 = bank.become_customer("Alice", "Moscow, Stremyannyi per, 1")
    customer2 = bank.become_customer("Bob", "Vorkuta, ul. Lenina, 5")

    # Alice opens an account and deposits some money
    alice_account = bank.create_account(customer1.id, initial_balance=500.0)
    alice_account.deposit(100.0)
    print(f"Alice's balance: {alice_account.balance}") # Alice's balance: 600.0

    # Bob opens an account and deposits some money
    bob_account = bank.create_account(customer1.id, initial_balance=1000.0)
    bob_account.deposit(500.0)
    print(f"Bob's balance: {bob_account.balance}")  # Bob's balance: 1500.0

    # Alice withdraws some money from her account
    alice_account.withdraw(300.0)
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 300.0

    # Alice tries to withdraw more money than she has in her account
    try:
        alice_account.withdraw(500.0)
    except ValueError as ex:
        print(ex)  # Insufficient funds

    retrieved_account = bank.get_account(alice_account.account_number)
    print(f"Account {retrieved_account.account_number} by {customer1.name} (customer_id: {retrieved_account.customer_id}), balance {retrieved_account.balance}") # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0

banking_scenario()