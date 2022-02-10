import store, product

uwajimaya = store.Store('uwajimaya')

yakisoba = product.Product(5001, 'Yakisoba Noodles', 5.99, 'International')
uwajimaya.list_of_products.append(yakisoba)
jumbo_shrimp = product.Product(4001, 'Shrimp 10-15ct.', 14.99, 'Seafood')
uwajimaya.list_of_products.append(jumbo_shrimp)
large_eggs = product.Product(2001, 'Large Eggs, Dozen', 1.69, 'Dairy')
uwajimaya.list_of_products.append(large_eggs)
whole_milk_halfgallon = product.Product(2002, 'Whole Milk, Half Gallon', 1.99, 'Dairy')
uwajimaya.list_of_products.append(whole_milk_halfgallon)

# print(f"{uwajimaya.list_of_products}")

for i in range(len(uwajimaya.list_of_products)):
    uwajimaya.list_of_products[i].print_info()

uwajimaya.inflation(.025)

for i in range(len(uwajimaya.list_of_products)):
    uwajimaya.list_of_products[i].print_info()

uwajimaya.set_clearance('International', .10)

for i in range(len(uwajimaya.list_of_products)):
    uwajimaya.list_of_products[i].print_info()

uwajimaya.sell_product(2001)

for i in range(len(uwajimaya.list_of_products)):
    uwajimaya.list_of_products[i].print_info()