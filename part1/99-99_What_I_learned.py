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