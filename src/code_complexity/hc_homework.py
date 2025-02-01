import math
import random

# Счет
class Account:
  def __init__(
      self,
      # Сущность банка содержит счета, открытые в нем. Нет смысла дублировать
      # эту информацию в сущности счета
      bank,
      account_number: int,
      # В данной сущности не имеет смысл хранить данные о клиенте
      # Это нарушает внутреннюю целостность (Cohesion)
      # Можно заменить на идентифкатор клиента
      customer_name: str,
      customer_address: str,
      balance: float):
    self.account_number = account_number
    self.balance = balance
    self.customer_name = customer_name
    self.customer_address = customer_address
    self.bank = bank

  # Внести
  def deposit(self, amount: float):
    # Привнесенная сложность - достаточно увеличивать данные поля self.balance
    # В дополнение - лишняя зависимость от другой сущности
    self.bank.accounts[self.account_number].balance += amount

  # Снять
  def withdraw(self, amount: float):
    # Привнесенная сложность, обращение к внешней сущности
    # amount <= self.balance
    if amount <= self.bank.accounts[self.account_number].balance:
      # Аналогично предыдущему комментарию
      self.bank.accounts[self.account_number].balance -= amount
    else:
      raise ValueError("Insufficient funds")

# Банк
class Bank:
  def __init__(self):
    self.accounts = {}
    # можно дополнить списком клиентов банка, чтобы убрать лишнюю зависимость из Customer

  def create_account(
      self,
      # Лучше определить переменнную-счетчик для того, чтобы задавать
      # уникальные идентификаторы счетов в рамках одной сущности банка
      # Это позволит поддерживать согласованное состояние объекта (Инкапсуляция)
      account_number: int,
      # Вместо name лучше использовать id пользователя
      customer_name: str,
      # Адрес имеет смысл хранить в сущности "Клиент", чтобы не смешивать
      # назначение классов (повысить целостность)
      customer_address: str,
      initial_balance: float) -> Account:
    account = Account(self, account_number, customer_name, customer_address, initial_balance)
    self.accounts[account_number] = account
    return account

  # Тут все ок
  def get_account(self, account_number: int) -> Account:
    if account_number in self.accounts:
      return self.accounts[account_number]
    else:
      raise ValueError("Account not found")

# Клиент
class Customer:
  def __init__(self, name: str, address: str, bank: Bank):
    # Для удобства и поддержания связи между счетом и клиентом,
    # имеет смысл присваивать каждому клиенту уникальный идентификатор
    self.name = name
    self.address = address
    # Для сущности клиент имеет смысл убрать излишнюю
    # зависимость от сущности банк
    self.bank = bank

  # Лишний функционал, снижает целостность
  def open_account(self, initial_balance: float) -> Account:
    account_number = self._generate_account_number()
    account = self.bank.create_account(account_number, self.name, self.address, initial_balance)
    return account

  # Лишний функционал, снижает целостность
  def _generate_account_number(self) -> int:
    return math.floor(random.random() * 1000000)


def banking_scenario():
  bank = Bank()
  customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
  customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)

  # Alice opens an account and deposits some money
  alice_account = customer1.open_account(initial_balance=500.0)
  alice_account.deposit(100.0)
  print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 600.0

  # Bob opens an account and deposits some money
  bob_account = customer2.open_account(initial_balance=1000.0)
  bob_account.deposit(500.0)
  print(f"Bob's balance: {bob_account.balance}")  # Bob's balance: 1500.0

  # Alice withdraws some money from her account
  alice_account.withdraw(300.0)
  print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 300.0

  # Alice tries to withdraw more money than she has in her account
  try:
    alice_account.withdraw(500.0)
  except ValueError as e:
    print(e)  # Insufficient funds

  # Bank retrieves Alice's account using the account number
  retrieved_account = bank.get_account(alice_account.account_number)
  print(f"Account {retrieved_account.account_number} by {retrieved_account.customer_name} ({retrieved_account.customer_address}), balance {retrieved_account.balance}") # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0
