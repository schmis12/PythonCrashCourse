# Stefan J, Schmidt, 14.03.2019

favorite_places = {
    'stefan': ['schlossberg', 'belchen', 'rhein', 'badberg', 'berlin'],
    'georg': ['hofweiher', 'badberg', 'hamburg'],
    'marion': ['berlin', 'toscana', 'mengen'],
}

for person, places in favorite_places.items():
    print("\n" + person.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())