import csv
# made by Rexsy
# concept
#1. get the name of the product
#2. get the price of the product
#3. get the quantities of the product
#4. If its done, then print the total price
#5. Elif not done, loop number 1
#6. opsional konsep = save the data to a csv

def product_name(): #get the name of the product
    while True:
        try:
            name = input("What is the name of the product : ").lower()
            if name.isalpha():
                return name
            elif name.isalpha() == False:
                print("Please enter the name of the product correctly")
        except AttributeError:
            print("Please enter the name of the product correctly")
    

def price(): #get the price of the product
    try:
        price = input("Price of the product (in IDR) : ")
        price = int(price)
    except ValueError: #fail mechanism if user input other than integer
        print("Please enter the price correctly in number")
    return price


def quantities(): #get the quantities of the product
    try:
        quantities = input("quantities of the product : ")
        quantities = int(quantities)
    except ValueError: #fail mechanism if user input other than integer
        print("Please enter the quantities correctly in number")
    return quantities


def get_product_data(name, price, quantities):
    #products = []
    name_val = name
    price_val = price
    quantity_val = quantities
    # Create a dictionary for this product and add it to the list
    product = {"Name": name_val, "Price": price_val, "Quantities": quantity_val}
    #products.append(product)
    return product
    
    

def calculation(harga, jumlah): #calculate the total price of a product (product*quantities) 
    totalproduct = harga*jumlah
    return totalproduct


def write_to_csv(data, filename):
    keys = data[0].keys()  # get the keys from the first dictionary
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == "__main__":
    totalharga = 0
    totalproduk = []
    while True:
        namaproduk = product_name()
        harga      = price()
        jumlah     = quantities()
        product    = get_product_data(namaproduk, harga, jumlah)
        print(type(product))
        totalharga = totalharga + calculation(harga,jumlah)
        totalproduk.append(product)
        more_products = input("Do you want to add more products? 1 for Yes, 0 for No: ")
        try:
            if int(more_products) == 1:
                continue
            elif int(more_products) == 0:
                break
        except ValueError:
            print("Please input the correct command, 1 for Yes continue to add more products. 0 for No")
            
    
print(totalproduk)
print(f"Total harga adalah {totalharga}")

write_to_csv(totalproduk, 'receipt.csv') #menulis ke file receipt.csv

#def main():
#    product_name()
#    price()
#    quantities()
#
#main()
#print()