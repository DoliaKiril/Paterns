from bill import Bill

class Customer:
    def __init__(self, ID, name, age, operator, balance, bill_limit):
        self.ID = ID
        self.name = name
        self.age = age
        self.operator = operator
        self.balance = balance
        self.bill_limit = bill_limit
        self.bills = []

    def talk(self, minutes, other_customer):
        if not isinstance(other_customer, Customer):
            print("Invalid operation. Please provide a valid Customer object.")
            return

        if self.operator and other_customer.operator:
            cost = self.operator.calculate_talking_cost(
                minutes, other_customer)

            if cost > 0:
                bill = Bill(self.ID, cost)
                self.bills.append(bill)
                other_customer.bills.append(bill)
                print(f"Talking cost added to bills: {cost}")
            else:
                print("Talking cost is zero. No bill generated.")
        else:
            print("No operators assigned to customers. Cannot talk.")

    def message(self, quantity, other_customer):
        if not isinstance(other_customer, Customer):
            print("Invalid operation. Please provide a valid Customer object.")
            return

        if self.operator and other_customer.operator:
            operator = self.operator
            cost = operator.calculate_message_cost(
                quantity, self, other_customer)

            if cost > 0:
                bill = Bill(self.ID, cost)
                self.bills.append(bill)
                other_customer.bills.append(bill)
                print(f"Message cost added to bills: {cost}")
            else:
                print("Message cost is zero. No bill generated.")
        else:
            print("No operators assigned to customers. Cannot send messages.")

    def connection(self, amount):
        if self.operator:
            operator = self.operator
            cost = operator.calculate_network_cost(amount)

            if cost > 0:
                bill = Bill(self.ID, cost)
                self.bills.append(bill)
                print(f"Network cost added to bills: {cost}")
            else:
                print("Network cost is zero. No bill generated.")
        else:
            print("No operators assigned to customers. Cannot connect to the internet.")
    def get_bills(self):

        return self.bills
