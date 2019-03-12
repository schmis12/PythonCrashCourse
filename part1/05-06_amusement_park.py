# Stefan J. Schmidt, 11.03.2019

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age >= 65:
    price = 5
else:
	price = 10

print(f"Your admission cost is ${price}.")