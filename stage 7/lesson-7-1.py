import os

class Product:
   def __init__(self,name, weight, category):
       self.name = name
       self.weight = weight
       self.category = category

   def __str__(self):
       return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = "products.txt"

    def get_products(self):
        if os.path.isfile(self.__file_name) == False:
            file = open(self.__file_name, "w")
            file.write("")
            file.close()
        file = open(self.__file_name,"r")
        goods = file.read()
        file.close()
        return goods

    def add(self,*products):
        exist_products = self.get_products()
        for product in products:
            if str(product) in exist_products:
                print(f"Продукт {product} уже есть в магазине")
            else:
                exist_products = exist_products + f"\n{product}"
        file = open(self.__file_name,"w")
        file.write(exist_products)
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
