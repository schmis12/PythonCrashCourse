# Stefan J. Schmidt, 09.03.2019

car = 'bmw'

print("Is car == 'subaru'? I predict False")
print(car == 'subaru')

print("\nIs car != 'subaru'? I predict True.")
print(car != 'subaru')

print("\nIs car.upper() == 'bmw'? I predict False.")
print(car.upper() == 'bmw')

print("\nIs car.upper() == 'BMW'? I predict True.")
print(car.upper() == 'BMW')

print("\nIs 1 > 0? I predict True")
print(1 > 0)

print("\nIs 1 > 1? I predict False")
print(1 > 0)

print("\nIs 1 >= 1? I predict True")
print(1 > 0)

print("\nIs 1 <= 1? I predict True")
print(1 > 0)

cars = ['toyota', 'bmw', 'audi', 'subaru']

print("\nIs 'bmw' in cars? I predict True")
print('bmw' in cars)

print("\nIs 'vw' not in cars? I predict True")
print('vw' not in cars)

print("\nIs 'audi' not in cars? I predict False")
print('audi' not in cars)

print("\nIs car in cars and car == 'audi'? I predict False")
print(car in cars and car == 'audi')

print("\nIs car in cars and car == 'bmw'? I predict True")
print(car in cars and car == 'bmw')


