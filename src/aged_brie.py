from src.variable_item import VariableItem

class AgedBrie(VariableItem):
    
    def update_quality(self):
        if self.quality <= 0: return
        if(self.sell_in > 0):
            self.quality += 1
        else:
            self.quality += 2