inventory = {}

sample_name = "Laptop"
sample_quantity = 5
sample_price = 799.99

categories = ["Electronics", "Home", "Office"]
product_ids = set()


def generate_product_id():
    new_id = 101
    while new_id in product_ids:
        new_id += 1
    product_ids.add(new_id)
    return new_id


def find_product_by_name(name):
    for product_id, item in inventory.items():
        if item["name"].lower() == name.lower():
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

    product_id = generate_product_id()
    brand_tuple = (brand,)

    inventory[product_id] = {
        "name": name,
        "category": category,
        "brand": brand_tuple[0],
        "quantity": quantity,
        "price": price
    }

    print("\nItem added successfully!")


def view_inventory():
    print("\nCurrent Inventory:")
    print("--------------------")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product_id, item in inventory.items():
            print(f"ID: {product_id} | Name: {item['name']} | Brand: {item['brand']} | Category: {item['category']}")
            print(f"Price: ${item['price']:.2f} | Quantity: {item['quantity']}")
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

        inventory[product_id]["quantity"] = new_quantity
        inventory[product_id]["price"] = new_price

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
        print(f"\n{removed_product['name']} removed successfully!")


def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("===========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")


def main():
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
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()