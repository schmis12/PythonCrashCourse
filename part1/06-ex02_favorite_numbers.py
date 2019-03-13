# Stefan J. Schmidt, 13.03.2019

favorite_numbers = {
    'stefan': 7,
    'georg': 4,
    'marion': 2,
    'moritz': 12,
    'lilit': 3,
    'rupert': 42,
    'devil': 666,
}

for n in favorite_numbers:
    print(f"{n.title()}'s favorite number is: {favorite_numbers[n]}")