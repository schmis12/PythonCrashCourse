# Stefan J. Schmidt, 13.03.2019

alien_0 = {'color': 'green', 'points': 5}

# access a dictionary's values
print(f"You just shot a {alien_0['color']} alien!")
print(f"And earned {alien_0['points']} points.")

# add key-value pairs to a dictionary 
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying dictionary values
alien_0['color'] = 'yellow'
print(alien_0)

# remove a key-value pair
del alien_0['points']
print(alien_0)