def buy_product (inventory, transactions, name, quantity, seller_id):
    if name in list(inventory.keys()):
        inv_quant = inventory[name]["quantity"]
        inv_price = inventory[name]["price"]
        if inv_quant - quantity >= 0:
            inventory[name]["quantity"] = inv_quant - quantity
            transactions['seller_id'] = seller_id
            transactions["name"] = name 
            transactions["sum"] = inv_price * quantity
            return inventory, transactions
        else:
            print ("We can't process this operation")
    else:
        print ("We can't process this operation")
