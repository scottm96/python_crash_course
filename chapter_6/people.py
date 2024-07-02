people = {
    'person1' : {
        'first_name' : 'jason',
        'last_name' : 'rivers',
        'age' : 21,
        'city' : 'burbank',
        },
    'person2' : {
        'first_name' : 'meredith',
        'last_name' : 'smith',
        'age' : 35,
        'city' : 'omaha',
        },
    'person3' : {
        'first_name' : 'kathy',
        'last_name' : 'mcgraw',
        'age' : 17,
        'city' : 'saskatoon',
        },
}

for person , deets in people.items():
    full_name = f"{deets['first_name']} {deets['last_name']}"
    print (f"\nthese are {person}'s ({full_name.title()}'s) details:")
    print (f"\tFirst Name: {deets['first_name'].title()}")
    print (f"\tLast Name: {deets['last_name'].title()}")
    print (f"\tAge: {deets['age']}")
    print (f"\tCity: {deets['city'].title()}")