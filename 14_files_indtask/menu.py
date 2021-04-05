class MenuItem:
    """Інгредієнти для кожного виду кави"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "вода": water,
            "молоко": milk,
            "кава": coffee
        }


class Menu:
    """Типи кави на замовлення"""
    def __init__(self):
        self.menu = [
            MenuItem(name="мак'ято", water=200, milk=150, coffee=24, cost=65.0),
            MenuItem(name="мокко", water=50, milk=0, coffee=18, cost=52.0),
            MenuItem(name="по-віденські", water=250, milk=50, coffee=24, cost=75.0),
            MenuItem(name="глясе", water=250, milk=110, coffee=20, cost=50)
        ]

    def get_items(self):
        """повернення всіх видів кави на замовлення"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """пошук типу кави на замовлення, повернення її наявності, якщо вона є в списку, інакше None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Вибачте, кава такого типу не готується. Буде готуватися у наступному семестрі")
