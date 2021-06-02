import unittest

from  ..models.category_model import Category
from  ..models.product_model import Product


class CategoryTest(unittest.TestCase):
    def test_category_model(self):
        self.category = Category("Acessórios", "blablabla")