# Fish-shaped bread inventory dictionary
inventory = {
    "Red Bean Bread": 10,
    "Custard Bread": 8,
    "Chocolate Bread": 5
}

def show_inventory():
    print("\n📦 Current Inventory")
    print("---------------------")
    for flavor, count in inventory.items():
        print(f"{flavor} : {count} pieces")

# Run the function
show_inventory()