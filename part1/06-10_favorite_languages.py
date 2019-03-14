# Stefan J. Schmidt, 14.03.2019

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name.title() + "'s favorite language is: " + 
            languages[0].title())
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")