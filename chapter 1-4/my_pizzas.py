pizzas = ['perpperoni', 'barbeque', 'hawaiian']
friend_pizzas = pizzas[:]
print (friend_pizzas)

pizzas.append('beef jerky')
friend_pizzas.append('vegetarian')

print (f'my favourite pizzas are:')
for pizz in pizzas:
    print (pizz)

print (f"\nmy friend's favourite pizzas are:")
for fpizz in friend_pizzas:
    print (fpizz)