class Product:
    def __init__(self, name, value, description, category):
        self.name = name
        self.value = value
        self.description = description
        self.category = category

    
    def __str__(self):
        return self.name + ", " + str(self.value) + ", " + self.description + ", " + self.category