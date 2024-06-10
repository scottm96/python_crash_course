for value in range(1,21):
    print (value)

million=range(1,1000001)

print (min(million))
print (max(million))
print (sum(million))

oddnum = range(1,21,2)
for odd in oddnum:
    print (odd)


threes = range(3,31,3)
for three in threes:
    print (three)

cubes = [cube**3 for cube in range(1,11)]
for number in cubes:
    print(f'\n{number}') 

#slicing a list 
queer = cubes[:7]
print (queer)


#looping through a slice 
players = ['charles','martina','michael','florence','eli'] 
for player in players[1:]:
    print(player.title())

#copying a list. do so by slicing but not including the the first and final index in the slice code
replayers=players[:]
print (replayers)

my_foods = ['pizza','falafel','carrot cake']
friend_food =my_foods[:]

print (f'my favorite foods are: {my_foods}')
print(f"\nmy friend's favorite foods are: {friend_food}")
my_foods.append('yams')
friend_food.append('wele')

print (f'my favorite foods are: {my_foods}')
print(f"\nmy friend's favorite foods are: {friend_food}")

