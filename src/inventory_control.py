class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self) -> None:
        self.buy_list = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.MINIMUM_INVENTORY[ingredient] <= self.buy_list[ingredient]:
                return False
            self.buy_list[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.buy_list

    def get_available_dishes(self):
        available = set(self.INGREDIENTS.keys())
        for ingredient in self.buy_list:
            if self.MINIMUM_INVENTORY[ingredient] <= self.buy_list[ingredient]:
                for dish, ingredients in self.INGREDIENTS.items():
                    if ingredient in ingredients:
                        available.discard(dish)
        return available
