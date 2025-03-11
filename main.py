"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Ladra
email: ladrapavel@email.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

username = input('username:')
password = input('password:')
print('----------------------------------------')
if username in users and users[username] == password:
    print(f'Welcome to the app, {username}\nWe have 3 texts to be analyzed.')
else:
    print('unregistered user, terminating the program..')
    exit()
print('----------------------------------------')
selection = int(input('Enter a number btw. 1 and 3 to select:'))
interpunkce = """,.!?/()}[{]><:'";"""
if selection in range(1,4):
    text_without = TEXTS[selection-1].translate(str.maketrans("","", interpunkce))
else:
    print('incorrect input, terminating the program..')
    exit()
print('----------------------------------------')

slova = text_without.split()
pocet_slov = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_string_count = 0
sum_num = 0
for slovo in slova:
    pocet_slov += 1
    if slovo.isdigit():
        numeric_string_count += 1
        cislo = int(slovo)
        sum_num = cislo + sum_num
    elif slovo.isupper():
        uppercase_count += 1
    elif slovo.islower():
        lowercase_count += 1
    elif slovo.istitle():
        titlecase_count += 1
print(f'There are {pocet_slov} words in the selected text.')
print(f'There are {titlecase_count} titlecase words.')
print(f'There are {uppercase_count} uppercase words.')
print(f'There are {lowercase_count} lowercase words.')
print(f'There are {numeric_string_count} numeric strings.')
print(f'The sum of all the numbers {sum_num}')

velikost = []
for slovo in slova:
    velikost.append(len(slovo))
maximum = max(velikost)

print(f'''----------------------------------------
LEN|  OCCURENCES{'|NR'.rjust(maximum)}
----------------------------------------''')

for hodnota in range(1, maximum + 1):
    pocet_slov_s_velikost =  velikost.count(hodnota)
    print(f'{hodnota:3d}|{pocet_slov_s_velikost * '*'}{'|'.rjust(maximum-pocet_slov_s_velikost+10)}{pocet_slov_s_velikost}')
