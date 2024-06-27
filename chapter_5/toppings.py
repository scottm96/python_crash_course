requested_topppings = ["mushrooms",'green peppers','extra cheese']

if requested_topppings == 'anchovies':
    print('hold the anchovies')


requested_topppings = ["mushrooms",'green peppers','extra cheese']
for req_top in requested_topppings:
    if req_top == 'green peppers':
       print('we are out of green peppers rn')
    else:
        print (f'adding {req_top}')
print (f'\nfinished making your pizza')

print(f'\nNEXT ORDER')
requested_topppings = []

if requested_topppings:
    for req_top in requested_topppings:
        if req_top == 'green peppers':
           print('we are out of green peppers rn')
        else:
           print (f'adding {req_top}')
else:
    print('are you sure you want a plain pizza?')

