pets = {
    'paws' : {
        'animal' : 'dog',
        'owners name' : "kelly"
        },
    'kiksy' : {
        'animal' : 'goat',
        'owners name' : "patrick"
        },
    'larry' : {
        'animal' : 'hamster',
        'owners name' : "bob"
        },
    }

for pet , pet_info in pets.items():
    print(f"\n{pet.title()} belongs to {pet_info['owners name']}. She's a {pet_info['animal']}\n")