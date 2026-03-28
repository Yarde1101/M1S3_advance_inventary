import csv


def save_csv(inventory):
    """Saves the inventory to a CSV file."""
    if not inventory:                              # Task 4: validate not empty
        print("Inventory is empty. Nothing to save.\n")
        return

    path = input("File name (e.g. inventory.csv): ").strip()

    try:                                           # Task 4: try/except
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "quantity"])
            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])
        print(f"Saved to {path}\n")

    except PermissionError:                        # Task 4: permission error
        print(f"Error: no permission to write to '{path}'.\n")
    except OSError as e:
        print(f"Error while saving: {e}\n")


def load_csv(inventory):
    """Loads products from a CSV file into the inventory."""
    path = input("File name to load: ").strip()

    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            header = next(reader, None)
            if header != ["name", "price", "quantity"]:   # Task 5: validate header
                print("Error: invalid header. Expected 'name,price,quantity'.\n")
                return

            products = []
            errors   = 0

            for row in reader:
                if len(row) != 3:                         # Task 5: exactly 3 columns
                    errors += 1
                    continue
                try:
                    name     = row[0].strip()
                    price    = float(row[1])
                    quantity = int(row[2])
                    if price < 0 or quantity < 0:         # Task 5: no negatives
                        raise ValueError
                    products.append({"name": name, "price": price, "quantity": quantity})
                except ValueError:
                    errors += 1                           # Task 5: count invalid rows

            if errors:
                print(f"Warning: {errors} invalid row(s) skipped.")

    except FileNotFoundError:
        print("File not found.\n")
        return
    except UnicodeDecodeError:
        print("Error: use UTF-8 encoding.\n")
        return

    if not products:
        print("No valid products found in file.\n")
        return

    # Task 5: ask overwrite or merge
    choice = input("Overwrite inventory? (Y/N): ").strip().upper()

    if choice == "Y":
        inventory.clear()
        inventory.extend(products)
        print(f"Loaded {len(products)} product(s) — overwrite.\n")
    else:
        # Merge policy: sum quantities, update price if different
        merged = 0
        for new in products:
            existing = next((p for p in inventory
                             if p["name"].lower() == new["name"].lower()), None)
            if existing:
                existing["quantity"] += new["quantity"]
                if existing["price"] != new["price"]:
                    existing["price"] = new["price"]
                merged += 1
            else:
                inventory.append(new)
        print(f"Loaded {len(products)} product(s) — merge ({merged} updated).\n")