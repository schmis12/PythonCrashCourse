favorite_number = 7

# modern: f-string does the conversion.
msg1 = f"My favorite number is {favorite_number}."
print(msg1)


# old fashioned: string is converted using the str() function.
msg2 = "My favorite number is " + str(favorite_number) + "."
print(msg2)