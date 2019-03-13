# Stefan J. Schmidt, 13.03.2019

available_toppings = ['mushrooms', 'olives', 'green peppers',
					  'pepperoini', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']



for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}')
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')
