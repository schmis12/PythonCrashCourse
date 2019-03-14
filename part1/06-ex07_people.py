# Stefan J, Schmidt, 14.03.2019

person_0 = {
    'first_name': 'stefan',
    'last_name': 'schmidt',
    'age': 51,
    'city': 'basel',
}

person_1 = {
    'first_name': 'marion',
    'last_name': 'zehrer',
    'age': 46,
    'city': 'berlin',
}

person_2 = {
    'first_name': 'georg',
    'last_name': 'hofstetter',
    'age': 50,
    'city': 'umkirch',
}


# list of people
people = [person_0, person_1, person_2]


for p in people:
    print("\nName: " + p['first_name'].title() + " " + p['last_name'].title())
    print("Age: " + str(p['age']))
    print("City: " + p['city'].title())