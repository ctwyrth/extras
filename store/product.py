class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.product_name = name
        self.price = float(price)
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"{self.product_name} - ${self.price:.2f} - {self.category} - {self.id}")
        return self