# 1-m
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} summa balansga qoshildi!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} summa balancdan olindi!")

    def info(self):
        print(f"Egasi: {self.owner}, balansi: {self.balance}")

b1 = BankAccount("Abdullaziz", 10000)
b1.info()

b1.deposit(90000)
b1.info()

b1.withdraw(10000)
b1.info()


# 2-m
class OnlineShop:
    def __init__(self, product_name, price, quantity):
        self.product = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        print(f"Jami: {total} so'm")

    def apply_discount(self, percent):
        total = self.price * self.quantity
        discount_price = total - (total * percent / 100)
        print(f"Chegirmadan keyin: {int(discount_price)} so'm")

    def infolar(self):
        print(f"Mahsulot: {self.product}")
        print(f"Narxi: {self.price}")
        print(f"Soni: {self.quantity}")


shop = OnlineShop("Olma", 10000, 3)

shop.infolar()
shop.total_price()
shop.apply_discount(10)
