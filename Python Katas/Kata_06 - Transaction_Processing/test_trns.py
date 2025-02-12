import unittest
from transactions import (
    add_transaction,
    get_total_spent,
    remove_transaction,
    update_transaction_amount,
    get_customer_transactions,
    get_all_customers,
    get_highest_spending_customer,
    get_lowest_spending_customer,
    get_average_spending,
    get_transaction_count,
    get_transactions_in_range,
    clear_all_transactions,
)

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.transactions = {}

    def test_add_transaction_valid(self):
        add_transaction(self.transactions, "Alice", "T001", 100)
        self.assertIn("T001", self.transactions)
        self.assertEqual(self.transactions["T001"]["customer"], "Alice")

    def test_add_transaction_duplicate_id(self):
        add_transaction(self.transactions, "Bob", "T002", 200)
        with self.assertRaises(ValueError):
            add_transaction(self.transactions, "Charlie", "T002", 150)

    def test_get_total_spent(self):
        add_transaction(self.transactions, "Alice", "T003", 50)
        add_transaction(self.transactions, "Alice", "T004", 70)
        self.assertEqual(get_total_spent(self.transactions, "Alice"), 120)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            add_transaction(self.transactions, "Dan", "T005", -20)

    def test_remove_transaction_valid(self):
        add_transaction(self.transactions, "Alice", "T006", 100)
        self.assertTrue(remove_transaction(self.transactions, "Alice", "T006"))
        self.assertNotIn("T006", self.transactions)

    def test_remove_transaction_invalid_id(self):
        self.assertFalse(remove_transaction(self.transactions, "Alice", "T999"))

    def test_update_transaction_amount_valid(self):
        add_transaction(self.transactions, "Alice", "T007", 100)
        self.assertTrue(update_transaction_amount(self.transactions, "Alice", "T007", 150))
        self.assertEqual(self.transactions["T007"]["amount"], 150)

    def test_update_transaction_amount_invalid_id(self):
        self.assertFalse(update_transaction_amount(self.transactions, "Alice", "T999", 150))

    def test_get_customer_transactions(self):
        add_transaction(self.transactions, "Alice", "T008", 100)
        add_transaction(self.transactions, "Alice", "T009", 200)
        transactions = get_customer_transactions(self.transactions, "Alice")
        self.assertEqual(len(transactions), 2)
        self.assertIn("T008", transactions)
        self.assertIn("T009", transactions)

    def test_get_all_customers(self):
        add_transaction(self.transactions, "Alice", "T010", 100)
        add_transaction(self.transactions, "Bob", "T011", 200)
        customers = get_all_customers(self.transactions)
        self.assertEqual(len(customers), 2)
        self.assertIn("Alice", customers)
        self.assertIn("Bob", customers)

    def test_get_highest_spending_customer(self):
        add_transaction(self.transactions, "Alice", "T012", 100)
        add_transaction(self.transactions, "Bob", "T013", 300)
        add_transaction(self.transactions, "Charlie", "T014", 200)
        self.assertEqual(get_highest_spending_customer(self.transactions), "Bob")

    def test_get_lowest_spending_customer(self):
        add_transaction(self.transactions, "Alice", "T015", 100)
        add_transaction(self.transactions, "Bob", "T016", 300)
        add_transaction(self.transactions, "Charlie", "T017", 200)
        self.assertEqual(get_lowest_spending_customer(self.transactions), "Alice")

    def test_get_average_spending(self):
        add_transaction(self.transactions, "Alice", "T018", 100)
        add_transaction(self.transactions, "Alice", "T019", 200)
        self.assertEqual(get_average_spending(self.transactions, "Alice"), 150)

    def test_get_transaction_count(self):
        add_transaction(self.transactions, "Alice", "T020", 100)
        add_transaction(self.transactions, "Alice", "T021", 200)
        self.assertEqual(get_transaction_count(self.transactions, "Alice"), 2)

    def test_get_transactions_in_range(self):
        add_transaction(self.transactions, "Alice", "T022", 100)
        add_transaction(self.transactions, "Alice", "T023", 200)
        add_transaction(self.transactions, "Alice", "T024", 300)
        transactions = get_transactions_in_range(self.transactions, "Alice", 150, 250)
        self.assertEqual(len(transactions), 1)
        self.assertIn("T023", transactions)

    def test_clear_all_transactions(self):
        add_transaction(self.transactions, "Alice", "T025", 100)
        add_transaction(self.transactions, "Bob", "T026", 200)
        clear_all_transactions(self.transactions)
        self.assertEqual(len(self.transactions), 0)

if __name__ == "__main__":
    unittest.main()