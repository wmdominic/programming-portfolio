#3-1. Names
friends = ['Sarah', 'morgan', ' jayce', 'kim ', ' austin ']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title().lstrip())
print(friends[3].title().rstrip())
print(friends[4].title().strip())

#3-2. Greetings
name = input("Name: ")
message = f"Hey there, {name}! Hope you've been having a great day today! Love, William."
print(message)

#Okay, that wasn't the exercise...
message = f"Hey there, {friends[0].title()}. Have a great day!"
print(message)

#3-3. Your Own List
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'brown']
message = f"I like the colors {colors[1]} and {colors[-3]},"
print(message)
message = f"but I hate the color {colors[3]}."
print(message)

#3-4. Guest List

guest_list = ['TOBY', 'PAM', 'OSCAR', 'MICHAEL', 'KEVIN']
message = f"Good Morning, {guest_list[0].title()}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)
message = f"Good Morning, {guest_list[1].title()}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)
message = f"Good Morning, {guest_list[2].title()}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)
message = f"Good Morning, {guest_list[3].title()}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)
message = f"Good Morning, {guest_list[4].title()}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)

#3-5. Changing Guest List
print(guest_list[4])
del (guest_list[4])
guest_list.insert(4, 'JIM')
print(guest_list)
message = f"Good Morning {guest_list[4]}. You have been invited to the Finer Things Club Luncheon this Afternoon."
print(message)

#Had some trouble. Remember you can append, insert, or replace/modify a value to put in the element you want to have in your code.

#3-6. More Guests
print(f"We decided to open the Finer Things club to more people and hold it in the conference room. We will be inviting Bob, Phyllis, and Stanley. Not Dwight.")
guest_list.insert(0, 'Stanley')
guest_list.insert(3, 'Bob Vance, Vance Refrigeration')
guest_list.append('Phyllis')
print(f"The following have been invited guests to the Finer Thing Lucheon this afternoon:\n{guest_list[0].title()}\n{guest_list[1].title()}\n{guest_list[2].title()}\n{guest_list[3].title()}\n{guest_list[4].title()}\n{guest_list[5].title()}\n{guest_list[6].title()}\n{guest_list[7].title()}")

#3-7. Shrinking Guest List
print(guest_list)

message = "We have decided to rescind our invitations to the Finer Things Club. Remembering our mission to retain fanciness and class, we have decided to keep our club closed. Sorry for any inconveinence."
print(message)

phyllis = guest_list.pop(7)
jim = guest_list.pop(6)
michael = guest_list.pop(5)
bob = guest_list.pop(3)
stanley = guest_list.pop(0)

message = f"Sorry {phyllis.title()}; You are no longer invited to the Finer Things Club Luncheon."
print(message)
message = f"Sorry {jim.title()}; You are no longer invited to the Finer Things Club Luncheon."
print(message)
message = f"Sorry {michael.title()}; You are no longer invited to the Finer Things Club Luncheon."
print(message)
message = f"Sorry {bob.title()}; You are no longer invited to the Finer Things Club Luncheon."
print(message)
message = f"Sorry {stanley.title()}; You are no longer invited to the Finer Things Club Luncheon."
print(message)

message = f"The only ones allowed to the Finer Things Luncheon are:\n{guest_list[0].title()}\t{guest_list[1].title()}\t{guest_list[2].title()}"
print(message)

del guest_list[2]
del guest_list[1]
del guest_list[0]
print(guest_list)

#3-8. Seeing the World

trips = ['New Orleans', 'London', 'Paris', 'New York', 'San Diego']
print(trips)
print("")
print(sorted(trips))
print("")
print(sorted(trips, reverse=True))
print("")
trips.reverse()
print(trips)
print("")
trips.reverse()
print(trips)
print("")
trips.sort()
print(trips)
print("")
trips.sort(reverse=True)
print(trips)
print("")

#3-9. Dinner Guests
guest_list = ['TOBY', 'PAM', 'OSCAR', 'MICHAEL', 'KEVIN']
print(len(guest_list))

#3.10 - Every Function