class Operator:
    def __init__(self, ID, name, talkingCharge, messageCost, networkCharge, discountRate):
        self.ID = ID
        self.name = name
        self.talkingCharge = talkingCharge
        self.messageCost = messageCost
        self.networkCharge = networkCharge
        self.discountRate = discountRate

    def calculate_talking_cost(self, minutes, other_customer):
        total_cost = minutes * self.talkingCharge
        if other_customer.age < 18 or other_customer.age > 65:
            total_cost *= (1 - self.discountRate)
        return total_cost

    def calculate_message_cost(self, quantity, customer, other_customer):
        total_cost = quantity * self.messageCost
        if customer.operator == other_customer.operator:
            total_cost *= (1 - self.discountRate)
        return total_cost

    def calculate_network_cost(self, amount):
        return amount * self.networkCharge
