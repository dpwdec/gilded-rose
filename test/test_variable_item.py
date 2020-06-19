from unittest import TestCase
from src.variable_item import VariableItem

class TestVariableItem(TestCase):

    def test_has_increment_quality(self):
        variable_item = VariableItem("Foo", 10, 10)
        self.assertTrue(hasattr(variable_item, "increment_quality"))

    def test_increment_quality(self):
        variable_item = VariableItem("Foo", 10, 10)
        variable_item.increment_quality(-1)
        self.assertEqual(variable_item.quality, 9)

    def test_increment_quality_lower_cap(self):
        variable_item = VariableItem("Foo", 10, 0)
        variable_item.increment_quality(-1)
        self.assertEqual(variable_item.quality, 0)

    def test_increment_quality_upper_cap(self):
        variable_item = VariableItem("Foo", 10, 50)
        variable_item.increment_quality(1)
        self.assertEqual(variable_item.quality, 50)

    def test_has_update_sell_in(self):
        """
        All variable items can update their sell_in
        """
        variable_item = VariableItem("Foo", 10, 10)
        self.assertTrue(hasattr(variable_item, "update_sell_in"))

    def test_update_sell_in(self):
        """
        update_sell_in() reduces sell_in by 1
        """
        variable_item = VariableItem('foo', 10, 10)
        variable_item.update_sell_in()
        self.assertEqual(variable_item.sell_in, 9)

    def test_has_update_quality(self):
        """
        All variable items can update their quality
        """
        variable_item = VariableItem("Foo", 10, 10)
        self.assertTrue(hasattr(variable_item, "update_quality"))

    def test_update_quality_is_capped(self):
        """
        update_quality() returns early None when passed 0
        """
        variable_item = VariableItem("Foo", 0, 0)
        self.assertEqual(variable_item.update_quality(), None)

    def test_update_quality_is_capped_below_zero(self):
        """
        update_quality() returns early None when passed < 0
        """
        variable_item = VariableItem("Foo", 0, -1)
        self.assertEqual(variable_item.update_quality(), None)
    