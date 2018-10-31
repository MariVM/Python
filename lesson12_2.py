#Restaurant “At Python’s”
	
import random

dishes_string = input('What would you like? ') # This is a string
#dishes_string = 'eggs, spam, eggs, spam, tomato juice, spam'
   
if len(dishes_string): 
	print('Please see time to cook dishes: ')

dishes_list = set(dishes_string.split(' '))
dishes = []

def random_integer():
	return random.randint(0, 60)

def dishes_menu():
	print (dishes_list.title().strip().capitalize(), '.' * (30-len(dishes)), random.randint (0, 60), 'min')
	pass

for dishes in dishes_list:
	dishes.append(dish.strip())
	print (dishes_menu())