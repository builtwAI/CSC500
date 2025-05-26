# Step 1 (modified based on user input) & Step 4 (ItemToPurchase update): Define the ItemToPurchase class
class ItemToPurchase:
   
    #Represents an item to be purchased, including its name, description, price, and quantity.
   
    def __init__(thing, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        
        # ItemToPurchase.
        #initialize item's name, description, price, and quantity.

            #item_name (str): The name of the item. Defaults to "none".
            #item_description (str): The description of the item. Defaults to "none".
            #item_price (float): The price of the item. Defaults to 0.0.
            #item_quantity (int): The quantity of the item. Defaults to 0.
        
        thing.item_name = item_name
        thing.item_description = item_description # Retained for compatibility with ShoppingCart
        thing.item_price = float(item_price)
        thing.item_quantity = int(item_quantity)

    def print_item_cost(thing):
        #Calculates the total cost for this item (price * quantity) and prints the item's name, quantity, price, and total cost for this item.
        # Example output: Bottled Water 10 @ $1 = $10
        
        total_cost = thing.item_price * thing.item_quantity
        # Retained robust formatting for price and total cost to handle decimals
        price_str = f"${int(thing.item_price)}" if thing.item_price == int(thing.item_price) else f"${thing.item_price:.2f}"
        total_cost_str = f"${int(total_cost)}" if total_cost == int(total_cost) else f"${total_cost:.2f}"
        print(f"{thing.item_name} {thing.item_quantity} @ {price_str} = {total_cost_str}")
        return total_cost

# Step 4: Build the ShoppingCart class
class ShoppingCart:
   
    #Manages a collection of items to be purchased by a customer.
   
    def __init__(thing, customer_name="none", current_date="January 1, 2020"):
        #customer_name (str): The name of the customer.
        #current_date (str): The current date.
       
        thing.customer_name = customer_name
        thing.current_date = current_date
        thing.cart_items = [] # List to store ItemToPurchase objects

    def add_item(thing, item_to_purchase):
        # Adds an item to the cart_items list.

        thing.cart_items.append(item_to_purchase)
        print(f"'{item_to_purchase.item_name}' added to cart.")

    def remove_item(thing, item_name_to_remove):
        item_found = False
        for i, item in enumerate(thing.cart_items):
            if item.item_name == item_name_to_remove:
                del thing.cart_items[i]
                item_found = True
                print(f"'{item_name_to_remove}' removed from cart.")
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(thing, item_to_modify):
        
        #Modifies an existing item's description, price, and/or quantity in the cart.
        item_found_in_cart = False
        # This object represents the default state. If item_to_modify has these values for a field,
        # it means the user did not intend to change that specific field.
        default_item_for_comparison = ItemToPurchase() 

        for item_in_cart in thing.cart_items:
            if item_in_cart.item_name == item_to_modify.item_name:
                item_found_in_cart = True
                # Check and update description if the passed description is not the default "none"
                if item_to_modify.item_description != default_item_for_comparison.item_description:
                    item_in_cart.item_description = item_to_modify.item_description
                
                # Check and update price if the passed price is not the default 0.0
                if item_to_modify.item_price != default_item_for_comparison.item_price:
                    item_in_cart.item_price = float(item_to_modify.item_price)
                
                # Check and update quantity if the passed quantity is not the default 0
                if item_to_modify.item_quantity != default_item_for_comparison.item_quantity:
                    item_in_cart.item_quantity = int(item_to_modify.item_quantity)
                
                print(f"'{item_in_cart.item_name}' modified.")
                break
        
        if not item_found_in_cart:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(thing):
        #Returns the total quantity of all items in the cart.
        num_items = 0
        for item in thing.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(thing):
        #Calculates the total cost of all items in the cart.
        total_cost = 0.0
        for item in thing.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(thing):
        #Outputs the total cost of items in the cart along with item details.
        #If the cart is empty, prints a message indicating so.
        print(f"\n{thing.customer_name}'s Shopping Cart - {thing.current_date}")
        num_items = thing.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        
        if not thing.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        
        print() 

        for item in thing.cart_items:
            item.print_item_cost() 

        total_cost = thing.get_cost_of_cart()
        total_cost_str = f"${int(total_cost)}" if total_cost == int(total_cost) else f"${total_cost:.2f}"
        print(f"\nTotal: {total_cost_str}")

    def print_descriptions(thing):
        #Outputs each item's name and description in the cart.
        print(f"\n{thing.customer_name}'s Shopping Cart - {thing.current_date}")
        print("\nItem Descriptions")
        if not thing.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        for item in thing.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Step 5: Implement the print_menu() function
def print_menu(cart):
    #Displays a menu of options to manipulate the shopping cart and processes user choices.
    user_choice = ''
    while user_choice != 'q':
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item details") 
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        user_choice = input("Choose an option:\n")

        if user_choice == 'a':
            print("\nADD ITEM TO CART")
            # Get item details from user
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            
            # Input validation for price
            while True:
                try:
                    item_price_str = input("Enter the item price:\n")
                    item_price = float(item_price_str)
                    if item_price < 0:
                        print("Price cannot be negative. Please enter a valid price.")
                        continue
                    break
                except ValueError:
                    print("Invalid input for price. Please enter a number (e.g., 3 or 1.50).")
            
            # Input validation for quantity
            while True:
                try:
                    item_quantity_str = input("Enter the item quantity:\n")
                    item_quantity = int(item_quantity_str)
                    if item_quantity < 0:
                        print("Quantity cannot be negative. Please enter a valid quantity.")
                        continue
                    break
                except ValueError:
                    print("Invalid input for quantity. Please enter a whole number (e.g., 1 or 10).")

            new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(new_item)

        elif user_choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            if not cart.cart_items:
                print("SHOPPING CART IS EMPTY. Nothing to remove.")
            else:
                item_to_remove_name = input("Enter name of item to remove:\n")
                cart.remove_item(item_to_remove_name)

        elif user_choice == 'c':
            print("\nCHANGE ITEM DETAILS")
            if not cart.cart_items:
                print("SHOPPING CART IS EMPTY. Nothing to change.")
            else:
                item_name_to_modify = input("Enter the name of the item to modify:\n")
                
                current_item_in_cart = None
                for item in cart.cart_items:
                    if item.item_name == item_name_to_modify:
                        current_item_in_cart = item
                        break
                
                if not current_item_in_cart:
                    print("Item not found in cart. Nothing modified.")
                else:
                    # Create an ItemToPurchase object that will hold the modifications.
                    # initialize with the item's name and default values for other fields.
                    # If a field is not changed by the user, it will retain its default here,
                    # and modify_item() will know not to update the cart if the value matches default.
                    mod_item_details = ItemToPurchase(item_name=item_name_to_modify)

                    # Modify Description
                    print(f"Current description: {current_item_in_cart.item_description}")
                    new_description_val = input("Enter new description (or press Enter to keep current):\n")
                    if new_description_val: # If user typed something
                        mod_item_details.item_description = new_description_val
                    # Else: mod_item_details.item_description remains "none" (default)

                    # Modify Price
                    print(f"Current price: {current_item_in_cart.item_price}")
                    while True:
                        new_price_input_str = input("Enter new price (or press Enter to keep current):\n")
                        if not new_price_input_str: # User pressed Enter, no change intended for price
                            break 
                        try:
                            temp_price = float(new_price_input_str)
                            if temp_price < 0:
                                print("Price cannot be negative. Please enter a valid price.")
                            else:
                                mod_item_details.item_price = temp_price # Set new price
                                break 
                        except ValueError:
                            print("Invalid input for price. Please enter a number.")
                    
                    # Modify Quantity
                    print(f"Current quantity: {current_item_in_cart.item_quantity}")
                    while True:
                        new_quantity_input_str = input("Enter new quantity (or press Enter to keep current):\n")
                        if not new_quantity_input_str: # User pressed Enter, no change intended for quantity
                            break
                        try:
                            temp_quantity = int(new_quantity_input_str)
                            if temp_quantity < 0:
                                print("Quantity cannot be negative. Please enter a valid quantity.")
                            else:
                                mod_item_details.item_quantity = temp_quantity # Set new quantity
                                break 
                        except ValueError:
                            print("Invalid input for quantity. Please enter a whole number.")
                            
                        cart.modify_item(mod_item_details)
    
        elif user_choice == 'i': 
            cart.print_descriptions()

        elif user_choice == 'o': 
            cart.print_total()
            print("Please pay at the counter.")

        elif user_choice == 'q':
            print("Quitting menu. Thank you for shopping!")

        else:
            print("Invalid option. Please try again.")

# Main section of the code
if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    my_cart = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {my_cart.customer_name}") 
    print(f"Today's date: {my_cart.current_date}")

    print_menu(my_cart)