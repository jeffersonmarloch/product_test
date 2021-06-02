from models.category_model import Category
from .dao import File  


class CategoryDAO:
    def __init__(self, name_file):
        self.name_file = name_file
        File.create(name_file)


    def insert(self, category): 
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
