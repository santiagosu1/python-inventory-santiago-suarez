# Python Inventory Management System

sample_name = "Notebook"   
sample_quantity = 10         
sample_price = 4.99           
inventory = {}

categories = ["Electronics", "Home", "Office", "Food"]
product_ids = set()

FILE_NAME = "inventory.txt"

class Product:
    def __init__(self, product_id, name, category, brand, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = (brand,)
        self.quantity = quantity
        self.price = price

    def update_product(self, new_quantity=None, new_price=None):
        if new_quantity is not None:
            self.quantity = new_quantity
        if new_price is not None:
            self.price = new_price

    def display_product(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {self.category}")
        print(f"Price: ${self.price:.2f} | Quantity: {self.quantity}")

    def to_file_string(self):
        return f"{self.product_id}|{self.name}|{self.category}|{self.brand[0]}|{self.quantity}|{self.price}|Normal"

    def get_type(self):
        return "Normal"


class PerishableProduct(Product):
    def __init__(self, product_id, name, category, brand, quantity, price, expiration_date):
        super().__init__(product_id, name, category, brand, quantity, price)
        self.expiration_date = expiration_date

    def display_product(self):
        super().display_product()
        print(f"Expiration Date: {self.expiration_date}")

    def to_file_string(self):
        return f"{self.product_id}|{self.name}|{self.category}|{self.brand[0]}|{self.quantity}|{self.price}|Perishable|{self.expiration_date}"

    def get_type(self):
        return "Perishable"


def generate_product_id():
    new_id = 101
    while new_id in product_ids:
        new_id += 1
    product_ids.add(new_id)
    return new_id


def find_product_by_name(name):
    for product_id, product in inventory.items():
        if product.name.lower() == name.lower():
            return product_id
    return None

def add_item():
    print("\nAdd New Item")
    print("-" * 20)

    name = input("Enter product name: ").strip().title()

    print("Available categories:")
    for category in categories:
        print(f"- {category}")

    category = input("Enter category: ").strip().title()

    if category not in categories:
        print("Invalid category. Item was not added.")
        return

    brand = input("Enter brand name: ").strip().title()

    try:
        quantity = int(input("Enter quantity: ").strip())
        price = float(input("Enter price: ").strip())
    except ValueError:
        print("Invalid quantity or price. Please enter numbers only.")
        return

    product_type = input("Is this a perishable product? (yes/no): ").strip().lower()

    product_id = generate_product_id()

    if product_type == "yes":
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ").strip()
        product = PerishableProduct(product_id, name, category, brand, quantity, price, expiration_date)
    else:
        product = Product(product_id, name, category, brand, quantity, price)

    inventory[product_id] = product
    print("\nItem added successfully!")


