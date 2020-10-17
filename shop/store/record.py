
import os

path_to_file = os.path.join('data', 'orders.txt')


def save_order(order):
    with open(path_to_file, mode='a') as orders_file:
        orders_file.write(str(order))
        orders_file.write('\n')


def load_orders():
    with open(path_to_file, mode='r') as order_file:
        return order_file.read()