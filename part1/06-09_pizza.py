# Stefan J. Schmidt, 14.03.2019

# store information about pizza ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza" +
    " with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)