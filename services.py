def add_product(inventory):
    """Adds a new product to the inventory."""
    name     = input("Name: ").strip()
    price    = float(input("Price: "))
    quantity = int(input("Quantity: "))
    if price < 0 or quantity < 0:
        print("Price and quantity must be >= 0.\n")
        return
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print("Product added.\n")


def show_inventory(inventory):
    """Displays all products in the inventory."""
    if not inventory:
        print("Inventory is empty.\n")
        return
    for p in inventory:
        print(f"  {p['name']} | $ {p['price']} | {p['quantity']} units")
    print()


def search_product(inventory):
    """Searches a product by name. Returns dict or None."""
    name = input("Product name: ").strip().lower()
    for p in inventory:
        if p["name"].lower() == name:
            print(f"Found: {p}\n")
            return p
    print("Product not found.\n")
    return None


def update_product(inventory):
    """Updates price and/or quantity of an existing product."""
    name = input("Product name to update: ").strip().lower()
    for p in inventory:
        if p["name"].lower() == name:
            new_price    = input("New price (Enter to skip): ").strip()
            new_quantity = input("New quantity (Enter to skip): ").strip()
            if new_price:
                if float(new_price) < 0:
                    print("Price must be >= 0.\n")
                    return
                p["price"] = float(new_price)
            if new_quantity:
                if int(new_quantity) < 0:
                    print("Quantity must be >= 0.\n")
                    return
                p["quantity"] = int(new_quantity)
            print("Updated.\n")
            return
    print("Product not found.\n")


def delete_product(inventory):
    """Removes a product from the inventory by name."""
    name = input("Product name to delete: ").strip().lower()
    for p in inventory:
        if p["name"].lower() == name:
            inventory.remove(p)
            print("Deleted.\n")
            return
    print("Product not found.\n")


def statistics(inventory):
    """Calculates and returns key inventory metrics."""
    if not inventory:
        print("Inventory is empty.\n")
        return None

    subtotal       = lambda p: p["price"] * p["quantity"]
    total_value    = sum(subtotal(p) for p in inventory)
    total_units    = sum(p["quantity"] for p in inventory)
    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock  = max(inventory, key=lambda p: p["quantity"])

    print(f"  Total value    : $ {total_value:.2f}")
    print(f"  Total units    : {total_units}")
    print(f"  Most expensive : {most_expensive['name']} ($ {most_expensive['price']})")
    print(f"  Highest stock  : {highest_stock['name']} ({highest_stock['quantity']} units)\n")

    return {
        "total_value":    total_value,
        "total_units":    total_units,
        "most_expensive": most_expensive,
        "highest_stock":  highest_stock,
    }