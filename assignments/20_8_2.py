def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit]=quantity
    return inventory[fruit]

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
print(new_inventory["strawberries"]==10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory)
print(new_inventory["strawberries"]==35)
