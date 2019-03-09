# Stefan J. Schmidt, 09.03.2019

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

print('2nd to 3rd element:')
print(players[1:3])

print('first two elements:')
print(players[:2])

print('last two elements:')
print(players[-2:])

print('looping through a slice:')
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())