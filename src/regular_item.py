from src.variable_item import VariableItem

class RegularItem(VariableItem):

    def update_quality(self):
        if self.sell_in > 0:
            self.increment_quality(-1)
        else:
            self.increment_quality(-2)