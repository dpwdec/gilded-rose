# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass_quality(item)
            elif item.name != "Sulfuras, Hand of Ragnaros":
                self._update_regular_item_quality(item)              
        
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

    def _change_quality(self, item, amount):
        item.quality += amount
        if item.quality > 50: item.quality = 50
        if item.quality < 0: item.quality = 0

    def _update_regular_item_quality(self, item):
        if item.sell_in < 0:
            self._change_quality(item, -2)
        else:
            self._change_quality(item, -1)

    def _update_aged_brie_quality(self, item):
        if item.sell_in < 0:
            self._change_quality(item, 2)
        else:
            self._change_quality(item, 1)

    def _update_backstage_pass_quality(self, item):
        if item.sell_in > 10:
            self._change_quality(item, 1)
        elif item.sell_in <= 10 and item.sell_in > 5:
            self._change_quality(item, 2)
        elif item.sell_in <= 5 and item.sell_in > -1:
            self._change_quality(item, 3)
        else:
            self._change_quality(item, -item.quality)

    def _reduce_quality(self, item):
        pass