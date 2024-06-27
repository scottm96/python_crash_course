usernames=['admin', 'fooseball3r', 'jamboree81', 'seklux8', 'jammingjay']
if usernames:
    for username in usernames:
        if username == 'admin':
            print('hello, admin would you like to see a status report ')
        else:
            print(f'hello, {username} thank you for logging in again')
else:
    print('we need to find some users')