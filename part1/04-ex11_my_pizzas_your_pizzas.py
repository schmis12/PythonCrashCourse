# Stefan J. Schmidt, 09.03.2019

pizzas = ['neapolitana', 'salami', 'funghi']
friend_pizzas = pizzas[:]

pizzas.append('vegetariana')
friend_pizzas.append('tonno')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friends favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)