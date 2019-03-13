# Stefan J Schmidt, 13.03.2019

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# new x-position
alien_0['x_position'] += x_increment

print(f"New x-position: {alien_0['x_position']}")