# Stefan J. Schmidt, 14.03.2019

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('The following languages have been mentioned:')

# remove duplicates by creation of a set
for language in set(favorite_languages.values()):
    print(language.title())