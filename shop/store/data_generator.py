import random

from store.order import Order
from store.order_element import OrderElement
from store.product import Product, ProductCategory


MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_quantity():
    return random.randint(MIN_QUANTITY, MAX_QUANTITY)


def generate_product(name=None):

    category = ProductCategory.FOOD
    unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
    identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)

    if name is None:
        name = f"Product - {identifier}"

    return Product(name, category, unit_price, identifier)


def generate_order_elements(number_of_product=None):
    if number_of_product is None:
        number_of_product = random.randint(1, Order.MAX_ELEMENTS)

    order_elements = []
    for product_number in range(number_of_product):
        product_name = f"Product - {product_number + 1}"
        product = generate_product(product_name)
        quantity = generate_quantity()
        order_elements.append(OrderElement(product, quantity))

    return order_elements
