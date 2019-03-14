# Stefan J, Schmidt, 14.03.2019

cities = {
    'berlin': {
        'country': 'germany',
        'population': 3900000,
        'fact': 'capital of germany',
    },
    'basel': {
        'country': 'switzerland',
        'population': 220000,
        'fact': 'switzerlands top location for pharmaceuticals and chemistry',
    },
    'mulhouse': {
        'country': 'france',
        'population': 303000,
        'fact': 'location of musee schlumpf',
    },
}

for city, info in cities.items():
    print(city.title())
    for k, v in info.items():
        print("\t" + k.title() + ": " + str(v).title())