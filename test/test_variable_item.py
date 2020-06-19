from unittest import TestCase
from src.variable_item import VariableItem

class TestVariableItem(TestCase):

    def test_has_update_quality(self):
        """
        All variable items can update their quality
        """
        variable_item = VariableItem("Foo", 10, 10)
        self.assertTrue(hasattr(variable_item, "update_quality"))
    