# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            if item.name == "Age Brie":
                pass
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                pass
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                self._update_regular_quality(item)
    
    def _update_regular_quality(self, item):
        item.quality -= 1
    
    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def _reduce_quality(self, item):
        pass