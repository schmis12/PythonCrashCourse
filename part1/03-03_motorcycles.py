
# append elements to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# replace 1st element
motorcycles[0] = 'ducati'
print(motorcycles)

# append an element
motorcycles.append('harley davidson')
print(motorcycles)

# inserting at 1st position
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

# removing an entry from a list
del motorcycles[0]
print(motorcycles)

# pop the last one off
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop off any position
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove an item by value
motorcycles.remove('suzuki')
print(motorcycles)

# remove by value using a variable
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
