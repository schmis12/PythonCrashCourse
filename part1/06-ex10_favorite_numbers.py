# Stefan J, Schmidt, 14.03.2019

favorite_numbers = {
    'stefan': [7, 77, 777],
    'georg': [4, 42, 50],
    'marion': [2, 4],
    'moritz': [12, 112, 212],
    'lilit': [3, 4, 5, 6],
    'rupert': [42],
    'devil': [666],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)