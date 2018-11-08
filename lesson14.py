#Restaurant “At Python’s”

import random

dishes_string = input('What would you like? ') # This is a string
#dishes_string = 'eggs, spam, eggs, spam, tomato juice, spam'
dish_list = []

class Dish:
    def __init__(self, name):
        self.name = name
    name_dish = 'tomato'

def calc_time():
    return random.randint(0, 100)

def to_print():
    print(unique_dish.ljust(20, '.'), calc_time(), 'min')
    pass

for dish in dishes_string.title().split(' '):
    dish_list.append(dish.strip())
unique_dish_list = set(dish_list)

for unique_dish in unique_dish_list:
    if unique_dish != '':
        to_print()