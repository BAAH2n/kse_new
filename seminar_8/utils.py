def is_valid_price(value):
    if value >= 0:
        return True
    else:
        return False
def is_valid_quantity (value):
    if value > 0:
        return True
    else:
        return False
def format_currency (amount):
    n = 0
    for i in str(amount):
        n += 1
    if n != 4:
        text = str(amount) + " грн"
    else:
        text = str(amount) + "0 грн"
    return text