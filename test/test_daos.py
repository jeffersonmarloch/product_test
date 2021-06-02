import unittest
import os.path
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from daos.category_dao import CategoryDAO
from daos.product_dao import ProdutoDAO
from models.category_model import Category
from models.product_model import Product


class TestDaos(unittest.TestCase):
    def test_create_category():
        categorydao = CategoryDAO("category.txt")
        category = Category("Acessório", "blablala")
        categorydao.insert(category.__str__())


    def test_create_product():
        productdao = ProdutoDAO("product.txt")
        product = Product("Pneu", 900, "blablala", "Acessório")
        productdao.insert(productdao.__str__())