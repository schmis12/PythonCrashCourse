# Stefan J. Schmidt, 14.03.2019

# let's start with an empty list for storing aliens
aliens = []

# make 30 aliens
for n in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# show first 5 aliens
print('\nFirst 5 aliens:')
for alien in aliens[:5]:
    print(alien)

# number of aliens
print('\nTotal number of aliens: ' + str(len(aliens)))