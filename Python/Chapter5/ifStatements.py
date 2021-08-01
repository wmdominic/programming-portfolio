#A SIMPLE if EXAMPLE:
'''cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#if-else STATEMENTS:
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("If you haven't registered yet or want more information on this year's election, please head over to: vote.org!")
else:
    print("\nI'm sorry, but you are too young to vote in this election.")
    print("Even though, please stay relevant and informed in our current political climate!")

#if-elif-else STATEMENTS:
age = 102

if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age >= 64:
    price = 30
elif age < 64:
   price = 40

print(f"Your admission is ${price}.")

#MULTIPLE CONDITIONS PAGE 83-84
requested_size = ['medium']
if 'small' in requested_size:
    print("Small pizza")
if 'medium' in requested_size:
    print("Medium pizza")
if 'large' in requested_size:
    print("Large pizza")

requested_toppings = ['mushrooms', 'sausage', 'pineapple']

if 'mushrooms' in requested_toppings:
    print("Add Mushroom")
if 'pepperoni' in requested_toppings:
    print("Add Pepperoni")
if 'sausage' in requested_toppings:
    print("Add Sausage")
if 'pineapple' in requested_toppings:
    print("Add Pineapple")
if 'extra cheese' in requested_toppings:
    print("Add Extra Cheese")

print("Your order has been submitted! Thank you!!")

#PAGE 86
requested_size = ['medium']

for size in requested_size:
    print(f"Pizza size: {size}")

requested_toppings = ['mushrooms', 'sausage', 'pineapple']

for requested_topping in requested_toppings:
    if requested_topping == 'sausage':
        print("Sorry, we are currently out of Sausage.")
    else:
        print(f"Adding {requested_topping}")

print("Your order has been placed. Thank you!")


#Page 87

pizza_size = 'medium'

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Add {requested_topping}")
    print("\nYour Order has been received. Thank you!")
else:
    print(f"Are you sure you want a plain {pizza_size} pizza??")

#Just messing around:
pizza_size = 'medium'
if pizza_size == 'small':
    print("small pizza")
if pizza_size == 'medium':
    print("medium pizza")
if pizza_size == 'large':
    print("large pizza")

requested_toppings = ['mushroom', 'pepperoni', 'onion']
if requested_toppings:
    for topping in requested_toppings:
        print(f"Add {topping}")
else:
    print(f"Are you sure you want a plain {pizza_size} pizza??")

print(f"Your order is a {pizza_size} pizza with {topping}.)
'''
#Multiple Lists

available_toppings = ['pepperoni', 'sausage', 'ham', 'green peppers', 'onions', 'mushrooms', 'tomatoes', 'pickles', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'saurkraut', 'pepperoni']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"ADD: {requested_topping.upper()}")
    else:
        print(f"ERROR: {requested_topping.title()} Unavailable.")

print("\nYour order had been placed")
