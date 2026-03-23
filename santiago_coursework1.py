inventory = {}

sample_name = "Laptop"
sample_quantity = 5
sample_price = 799.99

categories = ["Electronics", "Home", "Office"]
product_ids = set()


def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("===========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")


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


def main():
    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("Add Item option selected.")
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            print("Update Item option selected.")
        elif choice == "4":
            print("Remove Item option selected.")
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()