# Stefan J, Schmidt, 14.03.2019

cities = {
    'berlin': {
        'country': 'germany',
        'population': 3900000,
        'fact': 'capital of germany',
    },
    'basel': {
        'country': 'switzerland',
        'population': 200000,
        'fact': 'switzerlands top location for pharmaceuticals and chemistry',
    },
    'mulhouse': {
        'country': 'france',
        'population': 300000,
        'fact': 'location of musee schlumpf',
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}\nCountry: {info['country']}\nPopulation: {info['population']}\nFact: {info['fact']}")
