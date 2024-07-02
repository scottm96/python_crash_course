favorite_places = {
    'kira' : {
        'place1' : 'desert',
        'place2' : "gokart"
        },
    'beatrix' : {
        'place1' : 'local park',
        'place2' : 'paintball'
        },
    'clark' : {
        'place1' : 'farm house',
        'place2' : "basketball court"
        },
    }

for person , places in favorite_places.items():
    print (f"\n {person} loves going out a lot but are favourite places or activities are:")
    print (f"\t{places['place1']}")
    print (f"\t{places['place2']}")
