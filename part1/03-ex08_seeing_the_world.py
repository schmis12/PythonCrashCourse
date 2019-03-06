# Stefan Joachim Schmidt, 05.03.2019

# places I would like to see one day
places = ['London', 'Bamberg', 'Wuerzburg', 'Madeira', 'Costa Rica']

# original list
print(f"Original:{places})")

# temporary sorted
print(f"Sorted:{sorted(places)}")
print(f"Original:{places}")

# sorted reversed
print(f"Temp. reversed:{sorted(places, reverse = True)}")
print(f"Original:{places}")

# permanently reversed
places.reverse()
print(f"Reversed Original:{places}")
places.reverse()
print(f"Original:{places}")

# permanently sort
places.sort()
print(f"Sort Original:{places}")

# permanently reverse sort
places.sort(reverse=True)
print(f"Sort Reverse Original:{places}")