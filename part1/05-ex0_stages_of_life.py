# Stefan j. Schmidt, 12.03.2019

age = 67

if age < 2:
    stage = ' baby'
elif age < 4:
    stage = ' toddler'
elif age <  13:
    stage = ' kid'
elif age < 20:
    stage = ' teenager'
elif age < 65:
    stage = 'n adult'
else:
    stage = 'n elder'
print(f'The person is a{stage}.')