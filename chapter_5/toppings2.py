#using multiple lists 
available_ttoppings = ['mushrooms', 'olives', 'green peppers', 'pepperonni', 'pineapple','extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for req_top in requested_toppings:
    if req_top in available_ttoppings:
        print(f'adding {req_top}')
    else:
        print(f'sorry, we do not have {req_top}')
print('your pizza is ready')