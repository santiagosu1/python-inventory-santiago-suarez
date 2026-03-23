inventory = {}

sample_name = "Laptop"
sample_quantity = 5
sample_price = 799.99

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


class PerishableProduct(Product):
    def __init__(self, product_id, name, category, brand, quantity, price, expiration_date):
        super().__init__(product_id, name, category, brand, quantity, price)
        self.expiration_date = expiration_date

    def display_product(self):
        super().display_product()
        print(f"Expiration Date: {self.expiration_date}")

    def to_file_string(self):
        return f"{self.product_id}|{self.name}|{self.category}|{self.brand[0]}|{self.quantity}|{self.price}|Perishable|{self.expiration_date}"


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
    print("--------------------")

    name = input("Enter product name: ").strip().title()

    print("Available categories:")
    for category in categories:
        print("-", category)

    category = input("Enter category: ").strip().title()
    brand = input("Enter brand name: ").strip().title()
    quantity = int(input("Enter quantity: ").strip())
    price = float(input("Enter price: ").strip())
    product_type = input("Is this a perishable product? (yes/no): ").strip().lower()

    product_id = generate_product_id()

    if product_type == "yes":
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ").strip()
        product = PerishableProduct(product_id, name, category, brand, quantity, price, expiration_date)
    else:
        product = Product(product_id, name, category, brand, quantity, price)

    inventory[product_id] = product

    print("\nItem added successfully!")


def view_inventory():
    print("\nCurrent Inventory:")
    print("--------------------")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product in inventory.values():
            product.display_product()
            print()


def update_item():
    print("\nUpdate Item")
    print("--------------------")

    name = input("Enter product name to update: ").strip()
    product_id = find_product_by_name(name)

    if product_id is None:
        print("Product not found.")
    else:
        new_quantity = int(input("Enter new quantity: ").strip())
        new_price = float(input("Enter new price: ").strip())
        inventory[product_id].update_product(new_quantity, new_price)
        print("\nInventory updated successfully!")


def remove_item():
    print("\nRemove Item")
    print("--------------------")

    name = input("Enter product name to remove: ").strip()
    product_id = find_product_by_name(name)

    if product_id is None:
        print("Product not found.")
    else:
        removed_product = inventory.pop(product_id)
        product_ids.remove(product_id)
        print(f"\n{removed_product.name} removed successfully!")


def save_inventory_to_file():
    with open(FILE_NAME, "w") as file:
        for product in inventory.values():
            file.write(product.to_file_string() + "\n")


def load_inventory_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) >= 7:
                    product_id = int(parts[0])
                    name = parts[1]
                    category = parts[2]
                    brand = parts[3]
                    quantity = int(parts[4])
                    price = float(parts[5])
                    product_type = parts[6]

                    product_ids.add(product_id)

                    if product_type == "Perishable" and len(parts) == 8:
                        expiration_date = parts[7]
                        product = PerishableProduct(product_id, name, category, brand, quantity, price, expiration_date)
                    else:
                        product = Product(product_id, name, category, brand, quantity, price)

                    inventory[product_id] = product
    except FileNotFoundError:
        pass


def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("===========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")


def main():
    load_inventory_from_file()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("\nSaving inventory to file...")
            save_inventory_to_file()
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()