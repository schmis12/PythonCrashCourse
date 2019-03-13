# stefan J. Schmidt, 13.03.2019

glossary = {
    'dictionary': 'an object holding key-value pairs',
    'list': 'an object holding items like strings or numbers',
    'key': 'the identifier in a dictionary',
    'value': 'the value that can accessed by a key',
    'f-string': 'a modern method to represent variables in a string',
}

for entry in glossary:
    print(f"{entry}:\n\t{glossary[entry]}")