favorite_languages = {
    'jen': 'python',
    'tyler': 'rust',
    'kayce': 'go',
    'larry': 'rust',
    'pots': 'c',
    'fitz': 'python',
    }

language = favorite_languages['kayce'].title()
print(f"kayce's favorite language is {language}")

for person , language in favorite_languages.items():
    print (f"\n{person.title()}'s favorite programming language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())

friends = ['larry','tyler']
if 'eren' not in favorite_languages.keys():
        print('eren, please take the poll')

for name in favorite_languages.keys():
    print(f'hi {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, i can see you love {language}')


for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll')

print ('the following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
print(f'\n\n')

for language in set(favorite_languages.values()):
    print(language.title())

print(f'\n\n\n')
favorite_languages = {
    'jen': ['python' , 'C'],
    'tyler': ['rust', 'js'],
    'kayce': ['go'],
    'larry': ['rust'],
    'pots': ['c'],
    'fitz': ['python'],
    }

for name , languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f'\t{language.title()}')
    else:
        for language in languages:
            print(f"{name}'s favorite language is {language}")