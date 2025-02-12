def remove_transaction(transactions: dict, customer: str, transaction_id: str) -> bool:
    """Removes a transaction for a specific customer"""


def update_transaction_amount(transactions: dict, customer: str, transaction_id: str, new_amount: int) -> bool:
    """Updates the amount of a specific transaction for a customer"""


def get_customer_transactions(transactions: dict, customer: str) -> list:
    """Returns a list of all transactions for a specific customer"""


def get_all_customers(transactions: dict) -> list:
    """Returns a list of all unique customers in the transactions"""


def get_highest_spending_customer(transactions: dict) -> str:
    """Returns the customer who has spent the most in total"""


def get_lowest_spending_customer(transactions: dict) -> str:
    """Returns the customer who has spent the least in total"""


def get_average_spending(transactions: dict, customer: str) -> float:
    """Returns the average amount spent per transaction for a specific customer"""


def get_transaction_count(transactions: dict, customer: str) -> int:
    """Returns the total number of transactions for a specific customer"""


def get_transactions_in_range(transactions: dict, customer: str, min_amount: int, max_amount: int) -> list:
    """Returns a list of transactions for a customer within a specified amount range"""


def clear_all_transactions(transactions: dict) -> None:
    """Clears all transactions from the dictionary"""