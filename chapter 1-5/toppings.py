
requested_topping = 'mushrooms'

if requested_topping.lower() != 'anchovies':
	print('Hold the anchovies!')

requested_topping = ['mushrooms','onions','pineapple']

test = 'mushrooms' in requested_topping
print(test)


#5.3.6

requested_topping = ['mushrooms','extra cheese']

if 'mushrooms' in requested_topping:
	print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
	print('Adding pepperoni.')
if 'extra cheese' in requested_topping:
	print('Adding extra cheese.')
print('\nFinished making your pizza!')



#5.4.1

requested_toppings = []

#requested_toppings = ['mushrooms','green peppers','extra cheese']
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print('Sorry, we are out of green peppers right now.')
		else:
			print('Adding ' + requested_topping + '.')

	print('\nFinished making your pizza!')

else:
	print('Are you sure you want a plain pizza?')


available_toppings = ['mushrooms','olives','green peppers',
'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping + '.')
	else:
		print('Sorry,we dont have ' + requested_topping + '.')