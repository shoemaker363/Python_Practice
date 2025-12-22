class register:

    currency = "$"

    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.received = 0

    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.coins:
            self.received += int(input(f"How many {coin}?: ")) * self.coins[coin]
        return self.received

    def make_payment(self, cost):
        self.process_coins()
        if self.received >= cost:
            change = round(self.received - cost, 2)
            print(f"Here is your change of {self.currency}{change}.\n 'How does anyone overpay when they are paying in coins'🙄 ")
            self.profit += cost
            self.received = 0
            return True
        else:
            print("insufficient money, stop wasting our time!🤬\n 'coins are thrown at customer'")
            self.received = 0
            return False
