def add_product(inventory, name, price, quantity):
    if name in list(inventory.keys()):
        for key, value in inventory.items():
            if key == name:
                for key_2, value_2 in value.items():
                    if key_2 == "quantity":
                        inventory[key_2]=value_2+quantity
                        return inventory
                    else:
                        continue
            else:
                continue
    else:
        inventory[name] = {"price": price, "quantity": quantity}
        return inventory