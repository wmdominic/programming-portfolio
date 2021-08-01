#DICTIONARY
'''
alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

#ADDING TO A DICTIONARY
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#EMPTY DICTIONARY
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

#MODIFYING VALUES IN A DICTIONARY
alien_0 = {'x_position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original postion: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#REMOVING KEY-VALUE PAIRS
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
#Note: This has been removed PERMANENTLY!


#A DICTIONAARY OF SIMILAR OBJECTS
#instead of keeping information about one object in a dictionary,
#You can use a dictionary to store one aspect about many objects.

favorite_languages = {
    'jeremy': 'sql',
    'william': 'python',
    'elizabeth': 'html',
    'jayce': 'c++',
    'bri': 'html',
    }

language = favorite_languages['elizabeth'].upper()
print(f"Elizabeth's favorite language is {language}.")



#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)



#LOOPING THROUGH A DICTIONARY
user_0 = {
    'username': 'jkrovitz1',
    'first': 'jeremy',
    'last': 'krovitz'
    }


#.items() - for both key and value
for key, value in user_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.upper()}")

favorite_languages = {
    'jeremy': 'sql',
    'william': 'python',
    'elizabeth': 'html',
    'jayce': 'c++',
    'bri': 'html',
    }
friends = ['jayce', 'bri']

for name, language in favorite_languages.items():
    if language == 'python':
        print(f"\n{name.title()}'s favorite coding language is {language.title()}.")
    else:
        print(f"\n{name.title()}'s favorite coding language is {language.upper()}.")
print ("")

#.key() - looping through keys
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.upper()}!")

for name in sorted(favorite_languages.keys()):
    language = favorite_languages[name].title()
    print(f"{name.title()}, thank you for taking the poll. You responded {language.upper()}.")

#.values() - looping through values

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#This will display repeats.

for language in set(favorite_languages.values()):
    print(language.upper())
    
#This will display only one instance.    
'''
'''
#Nesting

#A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# //

aliens = []

#Make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 20

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

'''
#A List in a Dictionary

#Store information about a pizza being ordered
'''
pizza = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'sausage'],
}

#Summarize the order
print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

'''

pizza = {
    'quantity': 7,
    'crust': 'thick',
    'size': 'large',
    'cheese': 'normal',
    'toppings': ['lettuce', ' tomatoes', 'pickles', 'sausage', 'bananas', 'bacon', 'ranch', 'onions']
}

available_toppings = ['pepperoni', 'sausage', 'bacon', 'lettuce', 'tomatoes', 'pickles', 'peppers', 'olives', 'onions', 'no toppings']

for topping in pizza['toppings']:
    if topping not in available_toppings:
        print(f"Sorry, {topping} not available. Please choose something else.")
    if topping in available_toppings:
        print(f"Thank you for your order of {pizza['quantity']} {pizza['size'].title()} pizza(s) with {pizza['crust'].title()} crust, {pizza['cheese'].title()} amount of cheese, and the following toppings:")
        for topping in pizza['toppings']:
            print(f"\t{topping.title()}")