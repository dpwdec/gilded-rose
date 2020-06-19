from src.item import Item

class RegularItem(Item):

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.quality == 0: return
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2