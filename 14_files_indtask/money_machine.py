class MoneyMachine:

    CURRENCY = "грн. "

    COIN_VALUES = {
        "гривни, номінал 20 грн.": 20.0,
        "гривни, номінал 10 грн.": 10.0,
        "гривни, номінал 5 грн.": 5.0,
        "гривни, номінал 2 грн.": 2.0,
        "гривни, номінал 1 грн.": 1.0,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Вивід поточного доходу"""
        print(f"Ціна: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Повертає загальну кількість грошей прийнятих для оплати кави"""
        print("Вставте грошову купюру ")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Скільки купюр -  {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Повертає True, якщо замовлення сплачено, False, якщо грошей недостатньо."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Залишок {self.CURRENCY}{change} повернені.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Вибачте, але грошей не достатньо. Гроші повернені")
            self.money_received = 0
            return False
