import unittest
from shoppingCart import ShoppingCart
from Product import Product

class TestShoppingCartIntegration(unittest.TestCase):

    def test_addProduct_getCartTotal_integration(self):
        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        product1 = Product("Product 1", 10, 2)
        product2 = Product("Product 2", 5, 3)
        cart.addProduct(product1)
        cart.addProduct(product2)

        # Check if the cart total is correct
        total = cart.getCartTotal()
        expected_total = product1.calculateTotal() + product2.calculateTotal()
        self.assertEqual(total, expected_total, "Cart total calculation is incorrect")

    def test_getCartTotal_emptycart(self):
        # Create a shopping cart
        cart = ShoppingCart()

        total = cart.getCartTotal()
        self.assertEqual(total, 0, "Cart total should be zero when the cart is empty")

if __name__ == '__main__':
    unittest.main()
