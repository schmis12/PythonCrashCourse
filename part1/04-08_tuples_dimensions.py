# Stefan J. Schmidt, 09.03.2019

# create a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# TypeError: changing a tuple is not possible
#dimensions[0] = 250

# loop over a tuple
for dimension in dimensions:
    print(dimension)

# changing a tuple is not possible
# but creation of a tuple with the old ones name
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)