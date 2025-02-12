import unittest
from transactions import add_transaction, get_total_spent

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

if __name__ == "__main__":
    unittest.main()
