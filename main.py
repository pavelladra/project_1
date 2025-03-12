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
print('-' * 40)

if username in users and users[username] == password:
    print(f'Welcome to the app, {username}\nWe have 3 texts to be analyzed.')
else:
    print('unregistered user, terminating the program..')
    exit()
print('-' * 40)

selection = input('Enter a number btw. 1 and 3 to select:')
punct = """,.!?/()}[{]><:'";#$%&+_="""

if selection.isdigit(): 
    if int(selection) in range(1,4):
        clean_text = TEXTS[int(selection)-1].translate(str.maketrans("","", punct))
    else:
        print('number is out of range, terminating the program..')
        exit()
else:
    print('incorrect input, terminating the program..')
    exit()
print('-' * 40)

words = clean_text.split()
total_words = len(words)
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_string_count = 0
num_sum = 0

for word in words:
    if word.isdigit():
        numeric_string_count += 1
        num_sum = int(word) + num_sum
    elif word.isupper():
        uppercase_count += 1
    elif word.islower():
        lowercase_count += 1
    elif word.istitle():
        titlecase_count += 1

print(f'There are {total_words} words in the selected text.')
print(f'There are {titlecase_count} titlecase words.')
print(f'There are {uppercase_count} uppercase words.')
print(f'There are {lowercase_count} lowercase words.')
print(f'There are {numeric_string_count} numeric strings.')
print(f'The sum of all the numbers {num_sum}')

word_lengths = [len(word) for word in words]
max_length = max(word_lengths)

print(
    f'''{'-' * 40}
LEN|  OCCURENCES{'|NR'.rjust(max_length)}
{'-' * 40}'''
)

for length in range(1, max_length + 1):
    count =  word_lengths.count(length)
    print(f'{length:3d}|{'*' * count}{'|'.rjust(max_length-count + 10)}{count}')
