# Stefan J. Schmidt, 08.03.2019

# What I learned from this Python Crash Course

# 1. List Comprehensions
# create a list of squares
# using a for loop, but in only one line
squares = [value**2 for value in range(1, 11)]
print(squares)

# 2. Tuples
# tuples are similar to lists, but are immutable.
immutables = ('soil', 'wind', 'fire')
print(immutables)
# fails with TypeError:
#immutables[0] = 'earth'
# re-creation of the complete tuple is fine
immutables = ('earth', 'wind', 'fire')
print(immutables)

# 3. Empty List evaluates to False
favorite_books = []
if not favorite_books:
	print('Seems you are not a bookworm!')

# 4. Dictionary functions
user = {
    'username': 'schmis12',
    'f_name': 'Stefan',
    'l_name': 'Schmidt',
}
print(user.items())
print(user.keys())
print(user.values())

# 5. Set removes duplicates
print(set(['python', 'c', 'ruby', 'python']))

# 6. store user input
name = input("Enter your name: ")

# 7. cast numerical input
age = int(input("Enter your age: "))

