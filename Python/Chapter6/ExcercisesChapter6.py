'''#6-1. Person
william = {'first_name': 'william', 'last_name': 'lewandowski', 'age': 25, 'hometown': 'fargo, ND',}

name = william.get('first_name', 'No name found in data.').title()
print(name)

age_value = (william['age'])
print(age_value)

print(william['hometown'].upper())


#6-2. Favorite Numbers
favorite_numbers = {
    'william': 89, 
    'jeremy': 24, 
    'elizabeth': 200, 
    'michaela': 131, 
    'larry': 2,
    }

numb = favorite_numbers['william']
print(f"William's favorite number is: {numb}.")

numb = favorite_numbers['michaela']
print(f"Michaela's favorite number is: {numb}.")

#6-3. Glossary / 6-4. Glossary 2
glossary = {
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'In Python, a dictionary is a collection of key-value pairs.',
    'pop()': 'The pop() method removes the last item from a list permanently, but you you want to use that value.',
    'del': 'The del method removed an item from the list permanently and cannot be used elsewhere.',
    'range()': 'The range() function generates a series of numbers. If combines the with list() function, it can put those numbers generated into a list.',
    }

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

word = 'pop()'
print(f"\n{word.title()}: {glossary[word]}")

word = 'del'
print(f"\n{word.title()}: {glossary[word]}")

word = 'range()'
print(f"\n{word.title()}: {glossary[word]}")

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")

'''
#6-5. Rivers:
rivers = {
    'red': 'the United States', 
    'thames': 'England',
    'amazon': 'Brazil',
    }

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

#6.6 Polling

survey_participants = {
    'amanda': 'C++',
    'bill': 'Ruby',
    'carl': 'Python',
    'frank': 'HTML',
    'helen': 'CSS',
    'ingrid': 'Ruby',
    'john': 'PHP',
    'kevin': 'Python',
    'michael': 'Javascript',
    'olaf': 'CSS',
    'paulette': 'Ruby',
    'rachel': 'HTML',
    'stanley': 'Javascript',
    'travis': 'SQL',
    'wanda': 'Python',
    'xander': 'PHP',
    'yildiz': 'CSS',
    'zachariah': 'C++'
}

invite_list = ['amanda', 'bill', 'carl', 'devon', 'ellie', 'frank', 'gregory', 'helen', 'ingrid', 'john', 'kevin', 'lilith', 'michael', 'natalie', 'olaf', 'paulette', 'quincy', 'rachel', 'stanley', 'travis', 'ursula', 'valerie', 'wanda', 'xander', 'yildiz', 'zachariah']

for participant in invite_list:
    if participant in survey_participants:
        print(f"\nThank you, {participant.title()}, for taking the survey.")
    if participant not in survey_participants:
        print(f"\n{participant.title()}, please complete the survey. Your vote matters to us.")

for language in set(survey_participants.values()):
    print(language)