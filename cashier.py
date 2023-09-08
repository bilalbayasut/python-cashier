from Transaction import Transaction

def show_menu():
    print("\n====================")
    print("Self-Service Cashier")
    print("====================")
    print("1. Add Item")
    print("2. Update Item Name")
    print("3. Update Item Quantity")
    print("4. Update Item Price")
    print("5. Delete Item")
    print("6. Reset Transaction")
    print("7. Check Order")
    print("8. View Items")
    print("9. Calculate Total Price")
    print("0. Exit")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    transaction = Transaction()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':  # Add Item
            name = input("Enter item name: ")
            qty = get_float_input("Enter quantity: ")
            price = get_float_input("Enter price: ")
            transaction.add_item(name, qty, price)
            print("Item added successfully.")

        elif choice == '2':  # Update Item Name
            old_name = input("Enter the current item name: ")
            new_name = input("Enter the new item name: ")
            transaction.update_item_name(old_name, new_name)
            print("Item name updated successfully.")
        elif choice == '3':  # Update Item Quantity
            name = input("Enter the item name: ")
            qty = get_float_input("Enter new quantity: ")
            transaction.update_item_qty(name, qty)
            print("Item quantity updated successfully.")
        elif choice == '4':  # Update Item Price
            name = input("Enter the item name: ")
            price = get_float_input("Enter new price: ")
            transaction.update_item_price(name, price)
            print("Item price updated successfully.")
        elif choice == '5':  # Delete Item
            name = input("Enter the item name: ")
            transaction.delete_item(name)
            print("Item deleted successfully.")
        elif choice == '6':  # Reset Transaction
            transaction.reset_transaction()
            print("Transaction reset successfully.")
        elif choice == '7':  # Check Order
            print(transaction.check_order())
        elif choice == '8':  # View Items
            print(transaction.print_transaction())
        elif choice == '9':  # Calculate Total Price
            print("Total Price:", transaction.total_price_after_discount())
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()