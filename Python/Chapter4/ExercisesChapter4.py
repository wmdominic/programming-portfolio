#4-1. Pizzas
'''pizzas = ['mushroom and saurkraut', 'taco', 'Pickles Bacon Ranch']
for pizza in pizzas:
    print(f"{pizza.title()}")
    print(f"I love to eat {pizza.title()} pizza.\n")
print("Although, I really don't like to eat pizza...")

#4-2.Animals
exotic_animals = ['elephant', 'giraffe', 'ostrich', 'flamingo']
for animal in exotic_animals:
    print(f"{animal}s are so cool!")

#4-3. Counting to Twenty
twenty = list(range(21))
print(twenty)

#4-4. One Million & 4-5. Summing a Million

million_numbs = list(range(1, 1000001))


print(min(million_numbs))
print(max(million_numbs))
print(sum(million_numbs))

#4-6. Odd Numbers
odd_numbs = []
for value in range(1, 20, 2):
    odd_numbs.append(value)
    print(value)

#the first number is the beginning integer
#the second number is the ending integer -1
#the third number is the amount of numbers to out by. So if it was (0, 16, 5), the numbers 5, 10, and 15 would appear.

fives = []
for fiver in range(0, 501, 5):
    print(fiver)

#the variable 'value' does not need to be value, it can be whatever, but using the word value often helps us know that the output is going to be a new value.

#4-7. Threes. I already did this in my notes.
threes = []
for value in range(3, 31, 3):
    threes.append(value)
    print(value)

#4-8. Cubes (Oops accidentally did 4.9 as well by trying to be smart... Lol.)

cubes = [value**3 for value in range(1, 11)]
print(cubes)


#4-10. Slices
chemical_elements = ['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon']

print("The first three elements on the periodic table are:")
for element in chemical_elements[:3]:
    print(element)

print("\nThe following are gasses found on the second row of the periodic table:")
print(chemical_elements[5:9])

print("\nThis element is considered a noble gas:")
print(chemical_elements[9:])

#4-11. My Pizzas, Your Pizzas

my_pizzas = ['taco', 'mushroom', 'cheeseburger']
your_pizzas = my_pizzas[:]

my_pizzas.append('reuben')
your_pizzas.append('supreme')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("Your favorite pizzas are:")
for pizza in your_pizzas:
    print(pizza.title())'''

#4.12 More Loops
colors = ['red', 'orange', 'yellow', 'purple', 'blue', 'green']
colors.extend(['black', 'white'])
colors[4] = 'brown'
colors.remove('red')
colors.sort(reverse=True)
print(colors)
print(colors[:8:2])
print(colors[3:])

#4.13 Buffet
buffet_menu = ('hamburgers', 'hotdogs', 'chips', 'beans', 'coleslaw')
print("Our Menu for the week of June 7th:")
for item in buffet_menu:
    print(item.title())

buffet_menu = ('sloppy joes', 'chicken sammies', 'chips', 'beans', 'coleslaw')
print("\nOur Menu for the week of June 14th:")
for item in buffet_menu:
    print(item.title())
