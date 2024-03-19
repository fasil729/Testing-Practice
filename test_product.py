import unittest
from Product import Product

class TestProduct(unittest.TestCase):

    def test_calculateTotal(self):
        # Create a product
        product = Product("Test Product", 10, 2)

        # Calculate total
        total = product.calculateTotal()

        # Check if the total is correct
        self.assertEqual(total, 20, "Total calculation is incorrect")

    def test_zero_quantity(self):
        # Create a product with zero quantity
        product = Product("Test Product", 10, 0)

        # Calculate total
        total = product.calculateTotal()

        # Check if the total is zero
        self.assertEqual(total, 0, "Total should be zero when quantity is zero")

    def test_negative_price(self):
        # Create a product with negative price
        with self.assertRaises(ValueError):
            Product("Test Product", -10, 2)

    def test_negative_quantity(self):
        # Create a product with negative quantity
        with self.assertRaises(ValueError):
            Product("Test Product", 10, -2)

    def test_string_price(self):
        # Create a product with string price
        with self.assertRaises(TypeError):
            Product("Test Product", "10", 2)

if __name__ == '__main__':
    unittest.main()
