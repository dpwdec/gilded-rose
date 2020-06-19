# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                if item.sell_in < 0:
                    self._change_quality(item, 2)
                else:
                    self._change_quality(item, 1)
                item.sell_in = item.sell_in - 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality
                item.sell_in = item.sell_in - 1
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                if item.sell_in < 0:
                    self._change_quality(item, -2)
                else:
                    self._change_quality(item, -1)               
                item.sell_in = item.sell_in - 1

    def _change_quality(self, item, amount):
        item.quality += amount
        if item.quality > 50: item.quality = 50
        if item.quality < 0: item.quality = 0

    def _reduce_quality(self, item):
        pass