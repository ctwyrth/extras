class Store:
    def __init__(self, name):
        self.store_name = name
        self.list_of_products = []

    def add_product(self, new_product):
        self.list_of_products.append[new_product]

    def sell_product(self, id):
        for i in range(len(self.list_of_products)):
            if self.list_of_products[i].id == id:
                self.list_of_products[i].print_info()
                self.list_of_products.pop(i)
                break

    def inflation(self, percent_increase):
        for i in range(len(self.list_of_products)):
            self.list_of_products[i].update_price(percent_increase, is_increased = True)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.list_of_products)):
            if self.list_of_products[i].category == category:
                self.list_of_products[i].price -= (self.list_of_products[i].price * percent_discount)