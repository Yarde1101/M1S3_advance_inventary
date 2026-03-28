from services import add_product, show_inventory, search_product, update_product, delete_product, statistics
from files import save_csv, load_csv

inventory = []
option    = ""

while option != "9":
    print("1.Add  2.Show  3.Search  4.Update  5.Delete  6.Stats  7.Save  8.Load  9.Exit")
    option = input("Option: ").strip()

    if option == "1":
        add_product(inventory)
    elif option == "2":
        show_inventory(inventory)
    elif option == "3":
        search_product(inventory)
    elif option == "4":
        update_product(inventory)
    elif option == "5":
        delete_product(inventory)
    elif option == "6":
        statistics(inventory)
    elif option == "7":
        save_csv(inventory)
    elif option == "8":
        load_csv(inventory)
    elif option == "9":
        print("Goodbye!")
    else:
        print("Invalid option.\n")