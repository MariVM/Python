#Restaurant “At Python’s”
	
import random

dishes_string = input('What would you like? ') # This is a string
#dishes_string = 'eggs, spam, eggs, spam, tomato juice, spam'
   
if len(dishes_string): 
	print('Please see time to cook dishes: ')

dishes_list = dishes_string.split(',')
dishes_name = []
for dishes in dishes_list:
    dishes_name.append(dishes.strip().capitalize())
    random_integer = str(random.randint(0, 60))
    print(dishes + '.' * (30-len(dishes)) + random_integer + 'min')