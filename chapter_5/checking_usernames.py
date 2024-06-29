current_users= ['fooseball3r', 'Jamboree81', 'seklux8', 'jammingjay','dolly0x','gammerham']
current_userslower = []
for cu in current_users:
    cu = cu.lower()
    current_userslower.append(cu)
print(current_userslower)

new_users = ['jammingjay', 'yellowjack', 'mockingjay','loveangel','jamboree81']

for user in new_users:
    if user in current_userslower:
        print(f"sorry, but the username '{user}' is currently in use. please use another username")
    else:
        print('this username is avalable. click start to continue')