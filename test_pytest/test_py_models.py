import pytest
import os.path
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from models.category_model import Category
from models.product_model import Product



class TestCatalogModel:
    @pytest.fixture
    def py_test_category_model():
        

