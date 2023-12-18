class Bill:
    def __init__(self, customer_id, amount):
        self.customer_id = customer_id
        self.amount = amount
        self.current_debt = 0

    def check(self, amount):
        return self.current_debt + amount > self.limiting_amount

    def add(self, amount):
        if not self.check(amount):
            self.current_debt += amount
            print(f"Debt added: {amount}")
        else:
            print("Exceeds the limiting amount. Debt not added.")

    def pay(self, amount):
        if amount <= self.current_debt:
            self.current_debt -= amount
            print(f"Paid: {amount}")
        else:
            print("Invalid payment amount. Debt not paid.")

    def change_the_limit(self, amount):
        if amount >= 0:
            self.limiting_amount = amount
            print(f"Limiting amount changed to: {amount}")
        else:
            print("Invalid limiting amount. Limit not changed.")

    def get_limiting_amount(self):
        return self.limiting_amount

    def get_current_debt(self):
        return self.current_debt
