import unittest
from greedy_coin_algorithm import get_exact_change

class TestGetExactChange(unittest.TestCase):
    
    def test_exact_change(self):
        test_cases = [
            (19.99, {"$10 bill": 1, "$5 bill": 1, "$1 bill": 4, "quarter": 3, "dime": 2, "penny": 4}),
            (0.99, {"quarter": 3, "dime": 2, "penny": 4}),
            (100.00, {"$100 bill": 1}),
            (5.67, {"$5 bill": 1, "quarter": 2, "dime": 1, "nickel": 1, "penny": 2}),
            (0.41, {"quarter": 1, "dime": 1, "nickel": 1, "penny": 1}),
            (0.00, {}),  # Boundary case: no change required
            (0.01, {"penny": 1}),  # Smallest denomination
            (0.05, {"nickel": 1}),
            (0.10, {"dime": 1}),
            (1.00, {"$1 bill": 1}),  # One denomination
            (1000.00, {"$100 bill": 10}),  # Large value
        ]

        for amount, expected in test_cases:
            with self.subTest(amount=amount):
                result = get_exact_change(amount)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
