# Stefan J. Schmidt, 15.03.2019

number = int(input("Please enter a number: "))

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")