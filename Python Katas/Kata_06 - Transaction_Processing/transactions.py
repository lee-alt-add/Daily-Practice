
def add_transaction(transactions: dict, customer: str, transaction_id: str, amount: int) -> str:
    """Adds a transaction"""
    
    if transaction_id in transactions.keys():
        raise ValueError("Customer id already in use")
    
    transactions[transaction_id] = {"customer": customer, "amount": amount}


def get_total_spent(transactions: dict, customer: str) -> int:
    """Returns total amount spent by a customer"""
    total = 0
    for customer_id, values in transactions.items():
        if values['customer'] == customer:
            total += values['amount']
    
    return total
# c_dict = {}

# add_transaction(c_dict,"Alice", "T003", 50)
# add_transaction(c_dict,"Alice", "T004", 70)
# print(get_total_spent(c_dict, 'Alice'))
            