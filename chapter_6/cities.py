cities = {
    'new york' : {
        'country' : 'US',
        'population' : 'approximately 30 million',
        'fact' : 'Most famous city in the world'
        },
    'accra' : {
        'country' : 'ghana',
        'population' : 'approximately 3.5 million',
        'fact' : 'capital city of ghana'
        },
    'kumasi' : {
        'country' : 'ghana',
        'population' : 'approximately 2 million',
        'fact' : 'considered the second capital of Ghana'
        },
}

for city , facts in cities.items():
    print(f'welcome to {city.upper()} and this is what you need to know about this place')
    for key , value in facts.items():
        if value == 'US':
            print(f'\t{key.upper()} : {value.upper()}')
        else:
            print(f'\t{key.upper()} : {value.title()}')
