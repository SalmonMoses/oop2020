class CoffeeMaker:
    """Інгредієнти типів кави"""
    def __init__(self):
        self.resources = {
            "вода": 300,
            "молоко": 200,
            "кава": 100,
        }

    def report(self):
        """Всі інгредієнти типів кави"""
        print(f"Вода: {self.resources['вода']}мл.")
        print(f"Молоко: {self.resources['молоко']}мл.")
        print(f"Кава: {self.resources['кава']}г.")

    def is_resource_sufficient(self, drink):
        """Повернення True, якщо замовлення може бути виконане, інакше False """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Вибачте, недостатньо інгредієнту {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Визначення інгредієнтів, необхідних для приготування кави"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Ваше замовлення {order.name} ☕️. Дякуємо, що завітали до нас!")
