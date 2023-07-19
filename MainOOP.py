import csv

class Product:
    def __init__(self):
        self.name = self.get_product_name()
        self.price = self.get_price()
        self.quantities = self.get_quantities()

    def check_space(self, string): 
        return ' ' in string

    def get_product_name(self): 
        while True: 
            try: 
                name = input("What is the name of the product : ").lower() 
                if name.isalpha() or self.check_space(name): 
                    return name 
                else: 
                    print("Please enter the name of the product correctly") 
            except AttributeError: 
                print("Please enter the name of the product correctly") 

    def get_price(self): 
        while True: 
            try: 
                price = int(input("Price of the product (in IDR) : "))
                return price
            except ValueError: 
                print("Please enter the price correctly in number")    

    def get_quantities(self):
        while True: 
            try: 
                quantities = int(input("Quantities of the product : "))
                return quantities
            except ValueError: 
                print("Please enter the quantities correctly in number") 

    def calculate_total(self):
        return self.price * self.quantities

    def to_dict(self):
        return {"Name": self.name, "Price": self.price, "Quantities": self.quantities}


class Transaction:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product):
        self.products.append(product)
        self.total_price += product.calculate_total()

    def write_to_csv(self, filename): 
        keys = self.products[0].to_dict().keys()
        data = [product.to_dict() for product in self.products]
        with open(filename, 'w', newline='') as output_file: 
            dict_writer = csv.DictWriter(output_file, keys) 
            dict_writer.writeheader() 
            dict_writer.writerows(data) 

    def write_total_price(self, filename):
        with open(filename, 'w') as file: 
            file.write(f'Total price is {self.total_price}\n')


if __name__ == "__main__": 
    transaction = Transaction()
    while True: 
        product = Product()
        transaction.add_product(product)
  
        while True: 
            more_products = input("Do you want to add more products? 1 for Yes, 0 for No: ") 
            try: 
                if int(more_products) == 1: 
                    break 
                elif int(more_products) == 0: 
                    transaction.write_to_csv('receipt.csv')
                    transaction.write_total_price('totalharga.txt')
                    exit() 
                else: 
                    print("Please input the correct command, 1 for Yes continue to add more products. 0 for No") 
            except ValueError: 
                print("Please input the correct command, 1 for Yes continue to add more products. 0 for No") 
                continue
      
