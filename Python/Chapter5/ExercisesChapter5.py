#5-1. Conditional Tests
'''
color = 'orange'
print("Is my favorite color == 'orange'? I predict true.")
print(color == 'orange') #True

print("\nIs Jeremy's favorite color == 'orange'? I predict false.")
print(color == 'blue') #False

age = 15
print(age >= 18) #False
print(10 <= age) #True
print(age < 1) #False
print(age > 5) #True

drink = 'Water'
print(drink.lower() == 'water') #True
print(drink == 'Water') #True
print(drink == 'coke') #False

#5-2. More Conditional Tests

#5-3. Alien Colors 1
alien_color = 'red'
if 'green' in alien_color:
    print("5 Points")
elif 'yellow' in alien_color:
    print("10 Points")
elif 'red' in alien_color:
    print("25 Points")

alien_color = 'blue'
if 'green' in alien_color:
    print("5 Points")
elif 'yellow' in alien_color:
    print("10 Points")
elif 'red' in alien_color:
    print("25 Points")
#If the test fails, there will be no output

#5-4. Alien colors 2
alien_color = 'red'
if 'yellow' in alien_color:
    print("Yellow Alien Down - 10 Points!")
else:
    print("Red/Green Alien Down - 5 Points!")

alien_color = 'yellow'
if 'yellow' in alien_color:
    print("Yellow Alien Down - 10 Points!")
else:
    print("Red/Green Alien Down - 5 Points!")

#5-5. Alien Colors 3 - see 5-3...

#5-6. Stages of life

age = 99

if age < 2:
    print("This human is a baby.")
elif age < 5:
    print("This human is a toddler.")
elif age < 13:
    print("This human is a kid.")
elif age < 20:
    print("This human is a teenager.")
elif age < 65:
    print("This human is an adult.")
else:
    print("This human is an elder.")

#5-7. Favorite Fruit
favorite_fruits = ['pineapple', 'blueberry', 'clementine']

if 'pineapple' in favorite_fruits:
    print("Yummy! Pineapple!")
if 'banana' in favorite_fruits:
    print("Delicious! Banana!")
if 'clementine' in favorite_fruits:
    print("Zazzy! Clementine!")
if 'strawberry' in favorite_fruits:
    print("Succulent! Strawberry!")
if 'blueberry' in favorite_fruits:
    print("Outstanding! Blueberry!")
'''

#5-8. Hello Admin / #5-9. No Users

user_names = ['William95', 'Jeremy96', 'Larry55', 'Jayne75']
admin_accounts = ['Admin_1', "Admin_3", "Admin_Override"]
user = ['Karen65']

if user_names:
    for user_name in user_names:
         print(f"Hello {user_name}. What would you like to do?")
if admin_accounts:
    for admin in admin_accounts:
        print(f"Hello {admin}. Would you like a status report?")
if user not in user_names or admin_accounts:
    print("User not found. Please sign up.")

print("")

#5-10. Checking Usernames

current_users = ['William95', 'Jeremy96', 'Larry55', 'Jayne75', 'Karen65']
new_users = ['Anthony74', 'Vinny73', 'laRRy55', 'Elizabeth98', 'JaynE75']

current_users_lower = [user.lower() for user in current_users]
                        # Expression for item in list
#express user in lower caser for each user in the list current_users

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is UNAVAILABLE. Please choose a different user name.")
    else:
        print(f"{new_user} is AVAILABLE.")

#5-11. Ordinal numbers

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
