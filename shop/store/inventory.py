import csv
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

    @staticmethod
    def load_inventory(file_name="inventory.csv"):
        with open(file_name, newline="") as inventory:
            csv_inv = csv.reader(inventory)
            next(csv_inv)
            return [
                AvailableProduct(
                    quantity=int(row[4]),
                    name=row[0],
                    category=ProductCategory[row[1]],
                    unit_price=float(row[2]),
                    identifier=int(row[3])
                )
                for row in csv_inv
            ]


class Inventory:
    AVAILABLE_PRODUCTS = AvailableProduct.load_inventory()

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

    @staticmethod
    def update_csv(file_name="inventory.csv"):
        with open(file_name, mode="w", newline="") as inventory:
            csv_inv = csv.writer(inventory)
            csv_inv.writerow(["name", "category", "unit_price", "identifier", "quantity"])
            for product in Inventory.AVAILABLE_PRODUCTS:
                csv_inv.writerow([str(product.product.name),
                                  str(product.product.category.value.upper()),
                                  str(product.product.unit_price),
                                  str(product.product.identifier),
                                  str(product.quantity)]
                                 )
