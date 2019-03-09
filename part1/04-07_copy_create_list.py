# Stefan J. Schmidt, 09.03.2019

# additional reference to the same list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
# both references modify the same list
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f'my_foods: {my_foods}')
print(f'friend_foods: {friend_foods}')

# new list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# both references to to separate lists
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f'my_foods: {my_foods}')
print(f'friend_foods: {friend_foods}')