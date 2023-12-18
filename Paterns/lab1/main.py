from operator import Operator
from customer import Customer


operator1 = Operator(0, "Operator1", 0.2, 0.05, 0.05, 0.01)
operator2 = Operator(1, "Operator2", 0.3, 0.06, 0.03, 0.02)

customer1 = Customer(0, "Customer №1", 20, operator1, 100, 200)
customer2 = Customer(1, "Customer №2", 48, operator1, 150, 300)
customer3 = Customer(2, "Customer №3", 70, operator2, 200, 250)

customer1.talk(100, customer2)
customer2.message(20, customer3)
customer3.connection(500)

print("Customer №1 Bills:")
for bill in customer1.get_bills():
    print(f"Bill Amount: ${bill.amount}")

print("Customer №2 Bills:")
for bill in customer2.get_bills():
    print(f"Bill Amount: ${bill.amount}")

print("Customer №3 Bills:")
for bill in customer3.get_bills():
    print(f"Bill Amount: ${bill.amount}")
