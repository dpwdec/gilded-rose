from src.item import Item

class RegularItem(Item):

    def update_sell_in(self):
        self.sell_in -= 1