import random

from store.errors import TemporaryOutOfStock, ProductNotAvailable
from store.product import Product, ProductCategory


class AvailableProduct:

    def __init__(self, quantity, name, category, unit_price=None, identifier=None):
        if unit_price is None:
            unit_price = random.randint(1, 100)
        if identifier is None:
            identifier = random.randint(1, 100)

        self.quantity = quantity
        self.product = Product(name=name, category=category, unit_price=unit_price, identifier=identifier)


class Inventory:
    AVAILABLE_PRODUCTS = [
        AvailableProduct(quantity=100, name='Rolls', category=ProductCategory.FOOD),
        AvailableProduct(quantity=20, name='Bread', category=ProductCategory.FOOD),
        AvailableProduct(quantity=20, name='Cookies', category=ProductCategory.FOOD),
        AvailableProduct(quantity=10, name='Jam', category=ProductCategory.FOOD),
        AvailableProduct(quantity=10, name='Milk', category=ProductCategory.FOOD)
    ]

    @staticmethod
    def reserve_product(product, quantity):
        for available_product in Inventory.AVAILABLE_PRODUCTS:
            if available_product.product == product:
                if available_product.quantity >= quantity:
                    available_product.quantity -= quantity
                    return
                else:
                    raise TemporaryOutOfStock(product_name=product.name, available_quantity=available_product.quantity)
        raise ProductNotAvailable(product_name=product.name)
