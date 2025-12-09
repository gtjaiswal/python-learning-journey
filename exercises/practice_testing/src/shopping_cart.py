class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def get_item_count(self):
        return len(self.items)