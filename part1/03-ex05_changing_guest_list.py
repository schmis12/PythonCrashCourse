guests = ['linux torvalds', 'jesus christ', 'john coltrane', 'johann sebastian bach']
print(guests)

# unfortunately jesus can't make it
canceled = 'jesus christ'
c_idx = guests.index(canceled)

print(f"Unfortunately {canceled.title()} can't make it.")

# replace jesus with buddha
new_guest = 'siddhartha gautama'

print(f"We will invite {new_guest.title()} instead.")

guests.pop(c_idx)
guests.insert(c_idx, new_guest)

print(guests)