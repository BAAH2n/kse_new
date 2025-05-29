def add_transaction(transactions, amount, type, category):
    transactions ["Кількість грошей"] = amount
    transactions ["Тип"] = type
    transactions ["Категорія"] = category 
    return transactions
def get_balance(transactions):
    balance = 0
    for bdfsb, amount, reger in transactions.items():
        balance += amount
