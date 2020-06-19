from src.variable_item import VariableItem

class AgedBrie(VariableItem):
    
    def update_quality(self):
        if self.quality <= 0: return
        self.quality += 1