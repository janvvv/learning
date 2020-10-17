from dataclasses import dataclass

from store.product import Product


@dataclass
class OrderElement:
    product : Product
    quantity : int

    def calculate_price(self):
        return self.quantity * self.product.unit_price

    def __str__(self):
        return f'{self.product} x {self.quantity}'

