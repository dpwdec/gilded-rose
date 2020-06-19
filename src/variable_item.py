from src.item import Item

class VariableItem(Item):

    def update_sell_in(self):
        pass

    def update_quality(self):
        if self.quality <= 0: return