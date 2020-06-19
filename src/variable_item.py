from src.item import Item

class VariableItem(Item):

    def update_quality(self):
        if self.quality <= 0: return