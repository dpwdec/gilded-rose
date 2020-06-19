from src.item import Item

class VariableItem(Item):

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.quality <= 0: return

    def increment_quality(self, delta):
        self.quality += delta