from unittest import TestCase
from src.variable_item import VariableItem

class TestVariableItem(TestCase):

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
    