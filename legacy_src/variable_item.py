from src.item import Item

class VariableItem(Item):

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        pass

    def increment_quality(self, delta):
        self.quality += delta
        if(self.quality < 0): self.quality = 0
        if(self.quality > 50): self.quality = 50