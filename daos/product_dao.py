from models.product_model import Product
from .dao import File  

class ProdutoDAO:
    def __init__(self, name_file):
        self.name_file = name_file
        File.create(name_file)


    def insert(self, product: Product):
        File.write(self.name_file, product)


    def delete(self):
        '''

        '''
        return 0


    def list(self):
        product = File.read(self.name_file).splitlines()

        return product