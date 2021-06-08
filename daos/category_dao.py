import os.path
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from models.category_model import Category
from .dao import File  


class CategoryDAO:
    def __init__(self, name_file):
        self.name_file = name_file
        File.create(name_file)


    def insert(self, category: Category): 
        File.write(self.name_file, category)


    def delete(self):
        '''
  
        '''
        return 0


    def list(self):
        categories = File.read(self.name_file).splitlines()
        return categories


    @staticmethod
    def search_name(name_file, name):
        list_category = File.read(name_file).splitlines()
        for category in list_category:
            if name in category:
                return category[0]
