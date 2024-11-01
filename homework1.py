#დავალება N1

class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"


class House:
    def __init__(self, id, price, owner):
        self.id = id
        self.price = price
        self.owner = owner
        self.status = "For Sale"

    def sell(self, buyer, loan_amount=0):
        if loan_amount == 0:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold"
            print(f"House '{self.id}' has been sold to {buyer.name}.")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold with Loan"
            buyer.loan += loan_amount
            print(f"House '{self.id}' has been sold to {buyer.name} with a loan of {loan_amount}.")

    def __str__(self):
        return f"ID: {self.id}, Price: {self.price}, Owner: {self.owner.name}, Status: {self.status}"


owner = Person("Owner", deposit=5000)
buyer = Person("Buyer", deposit=2000)

house = House("123456", 3000, owner)

print(house)
house.sell(buyer)
print(house)

house2 = House("654321", 4000, owner)
print(house2)
house2.sell(buyer, loan_amount=1500)
print(house2)

print(owner)
print(buyer)

