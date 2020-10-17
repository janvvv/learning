import random


def products_delivery():
    available_products = [
        "Rolls"
        "Bread",
        "Cookies",
        "Apples",
        "Jam",
        "Orange",
        "Carrot",
        "Potato",
        "Cheese",
        "Milk"
    ]
    return [available_products[random.randint(0, 9)] for _ in range(5)]
