
def add_transaction(transactions: dict, customer: str, transaction_id: str, amount: int) -> str:
    """Adds a transaction"""
    
    if transaction_id in transactions.keys():
        raise ValueError("Customer id already in use")
    if amount <= 0:
        raise ValueError("Invalid amount")
    
    transactions[transaction_id] = {"customer": customer, "amount": amount}


def get_total_spent(transactions: dict, customer: str) -> int:
    """Returns total amount spent by a customer"""
    total = 0
    for customer_id, values in transactions.items():
        if values['customer'] == customer:
            total += values['amount']
    
    return total
            