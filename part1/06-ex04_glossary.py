# stefan J. Schmidt, 14.03.2019

glossary = {
    'dictionary': 'an object holding key-value pairs.',
    'list': 'an object holding items like strings or numbers.',
    'key': 'the identifier in a dictionary.',
    'value': 'the value that can accessed by a key.',
    'f-string': 'a modern method to represent variables in a string.',
    'set': 'a list with only unique items.',
    'sorted': 'a function that makes a sorted copy of your iterable.',
    'items': 'a dictonary function that returns a list of key/value pairs.',
    'keys': 'a dictionary function returning a list of keys.',
    'values': 'a dictionary function returning a list of values.'
}

for key, value in glossary.items():
    print(f"\n{key}:\n\t{value}")