from unittest import TestCase
from src.aged_brie import AgedBrie

class TestAgedBrie(TestCase):

    def test_update_quality(self):
        """
        Aged brie increases in quality
        over time
        """
        aged_brie = AgedBrie("Aged Brie", 10, 5)
        aged_brie.update_quality()
        self.assertEqual(aged_brie.quality, 6)