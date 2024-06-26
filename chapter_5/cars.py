cars=['audi', 'bmw','mercedez','honda']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print (car.title())

if 'audi' in cars:
    print('i knew you would have audi in the list')

if 'benz' not in cars:
    print('you no dey like benz?')