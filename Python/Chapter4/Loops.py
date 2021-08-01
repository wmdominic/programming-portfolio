'''chemical_elements = ['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon']
for element in chemical_elements:
    print(element)
for element in chemical_elements:
    print(element.title())
#If I take out the second loop, the code will do both prints at a time causing it to print 'hydrogen Hydrogen' 'helium Helium' etc.

for element in chemical_elements:
    print(f"Be Careful! {element.upper()} is a very dangerous chemical!")
    print(f"If you want to work or handle {element.upper()}, you need safety goggles, gloves, and an apron.\n")
print("Remember: Science can be fun while being safe!")

for value in range(1, 5):
    print(value)

#The code will only print UP TO the last number but not include it.
#So if you want the code to print out THROUGH five, you'll have to do:

for value in range(1,6):
    print(value)
    print("")

for value in range(6):
    print(value)
    print("")

#A single digit in the range will being the sequence at zero

numbers = list(range(6))
print(numbers)

even_numbs = list(range(2, 11, 2))
print(even_numbs)

squares = []   #empty list
for value in range(1, 11):   #loop through each value 1 to 10 using range function
    square = value ** 2    #each value is raised to the second power and assigned the variable square
    squares.append(square)    #each new value is appended to the list of squares

print(squares)

#This can be shortened by doing:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


threes = []
for value in range(3, 34, 3):
    threes.append(value)

print(threes)

#How to do this in one line of code

squares = [value**2 for value in range(1, 11)]
print(squares)

threes = [value for value in range(3, 34, 3)]
print(threes)

#WORKING WITH PART OF A LIST - a SLICE
#A slice, you specify the INDEX of the first and last elements you want to work with. Just like the range function, Python stops one item before the second index you specify. So if you say INDEX 4, it's going to only go through three.

presidents = ['washington', 'jefferson', 'lincoln', 'hoover', 'hayes', 'taft', 'carter']
print(presidents[0:3])

print(presidents[2:6])

#Omitting the first number results in it starting at the beginning of the list.
print(presidents[:5])

#and vice versa also applies. If you have your starting index but no ending index, it will go to the end of the list
print(presidents[4:])

#a third value can be placed, if added, it tells Python how many items to skip.
print(presidents[0::3])

#LOOPING THOUGH A SLICE
print("The following three presidents can be found on Mount Rushmore beside Theodore Roosevelt:")
for president in presidents[:3]:
    print(president.title())

my_foods = ['mac-n-cheese', 'spaghetti', 'tacos', 'sushi']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('shirmp')
friend_foods.append('blackberries')

print(my_foods)
print(friend_foods)'''

#TUPLES

dimensions = (200, 50)
print("original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nmodified dimensions")
for dimension in dimensions:
    print(dimension)
    

