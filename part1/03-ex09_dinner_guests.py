# Stefan J. Schmidt, 06.03.2019

# guest list
guests = ['linus torvalds', 'jesus christ', 'john coltrane', 'johann sebastian bach']
print(f"Initial guest list: {guests}.")
print(f"Initially I wanted to invite {len(guests)} guests to dinner.")

# insert new guest at 1st position
guests.insert(0, 'siddhartha gautama')

# insert new guest at 4th position
guests.insert(3, 'antichrist')

# append new guest
guests.append('wolfgang amadeus mozart')
print(f"Current guest list: {guests}.")
print(f"The current guest list has {len(guests)} guests.")

# not enough seats - we have to uninvite some guests
print("I'm so sorry, but I can only invite two guests for dinner!")

# remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest.title()}, I cannot invite you for dinner!")
    print(f"Still {len(guests)} guests invited...")

print(f"Still invited are: {guests}.")
print(f"Guest list has {len(guests)} entries.")

del guests[0:2]

print(f"Guest list is now empty: {guests}.")
print(f"Means, guest list has {len(guests)} entries.")