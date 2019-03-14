# Stefan J, Schmidt, 14.03.2019

hermin = {
    'name': 'hermin',
    'animal': 'rabbit',
    'owner': 'stefan',
}

bimbo = {
    'name': 'bimbo',
    'animal': 'dog',
    'owner': 'marion',
}

purzel = {
    'name': 'purzel',
    'animal': 'dog',
    'owner': 'bernd',
}

pets = [hermin, bimbo, purzel]

for pet in pets:
    print(f"{pet['name'].title()} was a {pet['animal'].title()} owned by {pet['owner'].title()}.")