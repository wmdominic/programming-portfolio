'''
my_dictionary = {
    'Author': 'Sylvia Plath',
    'Book': 'Ariel',
    'DOB': 'October 1932',
    'DOD': 'February 1963',
    }

for stat, info in my_dictionary.items():
    print(f"\n{stat.upper()}")
    print(f"{info}")
'''

'''
participants = {
    'kim': 'yes',
    'sarah': 'yes',
    'jayce': 'no',
    'bri': 'no',
    'katie': 'yes',
    'beatrice': 'no',
    'jeremy': 'yes',
    'larry': 'maybe',
    'karen': 'no',
}

volunteers = ['kim', 'jayce', 'jeremy', 'amber', 'jayne', 'bri', 'katie', 'larry', 'patrick', 'beatrice', 'karen', 'nick', 'sarah', 'amanda']

for name in volunteers:
    if name in participants.keys():
        print(f"Thank you, {name.title()}, for participating in our survey.")
    if name not in participants.keys():
        print(f"{name.title()}, please remember to take our survey. Thanks!")

'''

william = {'age': 25, 'gender': 'male', 'favorite color': 'orange',}
jeremy = {'age': 24, 'gender': 'male', 'favorite color': 'blue'}

boyfriends = [jeremy, william]

for boyfriend in boyfriends:
    if boyfriend['age'] == 24:
        print("Hey babe. You're amazing, and I love you.")
    else:
        print("\nLove, William.")