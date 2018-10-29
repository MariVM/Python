import random

dishes_string = input('What would you like? ') # This is a string
#dishes_string = 'eggs, spam, eggs, spam, tomato juice, spam'

if len(dishes_string): 
	print('Please see time to cook dishes: ')

#dishes_list = set(dishes_string.split(' '))
#dishes = []

dishes = [print(dishes.title().strip().capitalize(), '.' * (30-len(dishes)), random.randint (0, 60), 'min') for dishes in set(dishes_string.split(' '))]
