# Stefan J. Schmidt, 09.03.2019

foods = ('soup', 'pasta', 'main dish', 'dessert', 'salad')

for food in foods:
    print(food)

# does not work (immutable)
#food[0] = 'antipasta'
#food[-1] = 'fruit'

foods = ('antipasta', 'pasta', 'main dish', 'dessert', 'fruit')

for food in foods:
    print(food)
