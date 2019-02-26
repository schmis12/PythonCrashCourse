# Stefan J. Schmidt, 26.02.2019

# guest list
guests = ['linus torvalds', 'jesus christ', 'john coltrane', 'johann sebastian bach']
print(f"Initial guest list: {guests}.")

# insert new guest at 1st position
guests.insert(0, 'siddhartha gautama')

# insert new guest at 4th position
guests.insert(3, 'antichrist')

# append new guest
guests.append('wolfgang amadeus mozart')
print(f"Current guest list: {guests}.")

# print an invitation for every guest
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you for dinner!")

# not enough seats - we have to uninvite some guests
print("I'm so sorry, but I can only invite two guests for dinner!")

# remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest.title()}, I cannot invite you for dinner!")

print(f"Still invited are: {guests}.")

del guests[0:2]

print(f"Guest list is now empty: {guests}.")