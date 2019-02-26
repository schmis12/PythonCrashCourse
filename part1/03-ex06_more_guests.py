guests = ['linux torvalds', 'jesus christ', 'john coltrane', 'johann sebastian bach']
print(guests)

guests.insert(0, 'siddhartha gautama')
guests.insert(3, 'antichrist')
guests.append('wolfgang amadeus mozart')

print(guests)

for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you for dinner!")