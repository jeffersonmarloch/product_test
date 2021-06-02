import unittest
import os.path
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from  models.category_model import Category
from  models.product_model import Product


class ModelTest(unittest.TestCase):
    def test_category_model(self):
        category = Category("Acessórios", "blablabla")
        name = category.name
        description = category.description

        assert name == "Acessórios"
        assert description == "blablabla"

    def test_product_model(self):
        product = Product("Pneu", 900, "blabla", "Acessórios")
        name = product.name
        value = product.value
        description = product.description
        category = product.category


        assert name == "Pneu"
        assert description == "blabla"
        assert value == 900
        assert category == "Acessórios"


if __name__ == "__main__":
        unittest.main()
