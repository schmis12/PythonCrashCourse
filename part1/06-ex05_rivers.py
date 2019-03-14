# Stefan J. Schmidt, 14.03.2019

rivers = {
    'nile': 'egypt',
    'rhine': 'germany',
    'amazonas': 'brazil',
    'mekong': 'vietnam',
    'jangtse': 'china',
}

for k, v in rivers.items():
    print('The ' + k.title() + ' runs through ' + v.title() + '.')

print("\nRivers:")
for river in rivers.keys():
    print("\t" + river.title())

print("\nCountries:")
for country in rivers.values():
    print("\t" + country.title())