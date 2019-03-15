# Stefan J. Schmidt, 15.03.2019

guest_count = int(input("How many people are in your dinner group? "))

if guest_count > 8:
    print(str(guest_count) + "! Sorry, you have to wait for a table.")
else:
    print("Your table for " + str(guest_count) + " guests is ready!")