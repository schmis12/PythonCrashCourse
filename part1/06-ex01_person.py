# Stefan J. Schmidt, 13.03.2019

person = {
    'first_name': 'stefan',
    'last_name': 'schmidt',
    'age': 51,
    'city': 'basel',
}

# dictionary
print(person)

# values in a f-string
print(f"My name is {person['first_name'].title()} {person['last_name'].title()}." +
    f" I'm {person['age']} years old and live in {person['city'].title()}.")