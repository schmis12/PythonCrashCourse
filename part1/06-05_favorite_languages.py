# Stefan J. Schmidt, 14.03.2019

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() +
        "'s favorite language is " +
        language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

# since .keys() is the default when looping
# over a dictionary, this is sufficient:
for name in favorite_languages:
    print(name.title())

# use sorted() to sort keys (usually they're not)
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")