age = 900

if age < 2:
    stage = ' baby'
elif age < 4:
    stage = ' toddler'
elif age < 13:
    stage = ' kid'
elif age < 20:
    stage = ' teenager'
elif age < 65:
    stage = 'n adult'
else:
    stage = 'n elder'

print(f'you are a{stage}')