# Stefan J. Schmidt, 26.02.2019

# permanently sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Oringinal list:\t{cars}")
# sort list permanently
cars.sort()
print(f"Sorted list:\t{cars}")

# in reverse order
cars.sort(reverse = True)
print(f"Reverse list:\t{cars}")


# temporarily sorting a list with sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Temp. sorted:\t{sorted(cars)}")

# print original list
print(f"Original list:\t{cars}")

# reverse the original order (without sorting)
cars.reverse()
print(f"Reversed list:\t{cars}")

# length of a list
print(f"Our list of cars has length {len(cars)}.")