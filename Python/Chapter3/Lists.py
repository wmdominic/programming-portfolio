colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'green']
print(colors)

print(colors[0])

print(colors[4].title())

print(colors[1].title())
print(colors[3].title())

print(colors[-1].upper())
#By asking for item at index -1, Python always returns the last item in the list.
#This convention extends to other negative index values was well. The index -2 returns the second item from the end, -3 returns the third item from the end, and so on.

message = f"My favorite color is {colors[-2]}."
print(message)

#MODIFYING ELEMENTS IN A LIST pg. 36
colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'green']
print(colors)
colors[5] = 'white'
print(colors)

#You can change an element in the array or list directly by reassigning/changing the value.

#ADDING ELEMENTS TO A LIST pg. 37

colors.append('black')
print(colors)

#append adds tp the end of the list without affecting any other elements.
colors.extend(['pink', 'turquoise', 'brown'])
print(colors)
#extend can add multiple items at the end.

#INSERTING ELEMENTS TO A LIST pg. 38
colors.insert(3, 'indigo')
print(colors)

#REMOVING ELEMENTS
del colors[3]
print(colors)

#pop()
popped_colors = colors.pop()
print(colors)
print(popped_colors)
best_color = colors.pop(4)
print(f"The best color in the list is {best_color.title()}. Just saying...")

#REMOVE VALUE (not element)
#colors.remove('turquoise')
#print(colors)

special_color = 'turquoise'
colors.remove(special_color)
print(colors)
print(f"\n{special_color.upper()} is too specific for our list of colors.")
print(" ")

#ORGANIZING LISTS pg. 43

dog_breads = ['german sheppard', 'rottweiler', 'black lab', 'poodle', 'chihuahua']
dog_breads.sort()
print(dog_breads)

dog_breads = ['german sheppard', 'rottweiler', 'black lab', 'poodle', 'chihuahua']
dog_breads.sort(reverse=True)
print(dog_breads)

#The above is permanent sorting
print(" ")
#The below is temporary sorting
dog_breads = ['german sheppard', 'rottweiler', 'black lab', 'poodle', 'chihuahua']
print(sorted(dog_breads))
print(dog_breads)
print(sorted(dog_breads, reverse=True))
print(dog_breads)
print(" ")
#reverse order of original line-up - this is permanent but can be undone by applying the .reverse() again.
dog_breads.reverse()
print(dog_breads)
print(" ")
dog_breads.reverse()
print(dog_breads)
print(" ")

print(len(dog_breads))
