# Stefan J. Schmidt, 14.03.2019

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['stefan', 'damla', 'sarah', 'sascha', 'phil']

for user in users:
    if user in favorite_languages.keys():
        print('Thanks for responding, ' + user.title() + '!')
    else:
        print(user.title() + ' what abount joining our poll?')