from enum import Enum

from store.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from store.order import Order
from store.record import save_order, load_orders
from store.inventory import Inventory


class Action(Enum):
    NEW_ORDER = '1'
    HISTORY = '2'


def handle_customer():
    say_hello()
    selected_action = select_action()
    if selected_action is Action.NEW_ORDER:
        order = init_order()
        while more_products():
            add_product_to_order(order, Inventory.AVAILABLE_PRODUCTS)
        print_order_summary(order)
        save_order(order)
    else:
        show_history()


def say_hello():
    print('Welcome!')


def select_action():
    selected_action = input('For new order type 1, for history type 2: ')
    try:
        return Action(selected_action)
    except ValueError:
        print('Wrong number, please choose 1 or 2')
        return select_action()


def show_history():
    orders = load_orders()
    print(orders)


def init_order():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    return Order(first_name, last_name)


def more_products():
    selection = input('Type 1 to add products, type 2 to finish order: ')
    if selection != '1' and selection != '2':
        print('Choose 1 or 2')
        return more_products()
    return selection == '1'


def add_product_to_order(order, available_products):
    print('Here are available products:')
    for index, available_product in enumerate(available_products):
        print(f'{index} {available_product.product}')

    try:
        product_index_str = input('Choose number representing product: ')
        product_index = parse_product_index(product_index_str, max_index=len(available_products)-1)

        quantity_str = input('How many do You want to buy? ')
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(input_error)
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f'Only {error.available_quantity} of {error.product_name} available')
    except ProductNotAvailable as error:
        print(f'{error.product_name} not available')


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput(f'Choose number')

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f'Choose between 0 - {max_index}')

    return product_index


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput(f'Choose number')

    if quantity < 1:
        raise NotValidInput(f'Pick minimum 1')

    return quantity


def print_order_summary(order):
    print('Order:')
    print(order)
    print('Thank You!')
