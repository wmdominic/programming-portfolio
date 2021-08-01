'''guest_list = ['jeff', 'mary', 'randall', 'timothy']

for guest in guest_list:
    print(f"Welcome, {guest.title()}! You have been invited to Shelley's SURPRISE Birthday Party!")

guest_list[2] = 'phillip'
print(guest_list)

guest_list.insert(0, 'malachai')
guest_list.insert(3, 'harrold')
guest_list.append('charlene')

print(guest_list)

guest_list = ['malachai', 'jeff', 'mary', 'timothy', 'charlene']

for guest in guest_list:
    if guest in guest_list[2:]:
        popped_guest = guest_list.pop()
        print(f"Sorry {popped_guest.title()}, we ran out of room.")
    else: 
        if guest not in guest_list[2:]:
            print(f"{guest.title()}, you are still invited to the party.")

print(f"{guest_list}")



#This won't work because we need to use a while loop... As the loop deletes/pops the index, it re-evaluates the list, seeing a different index each time.
'''
print("Jeremy loves William!")

poets = ['W. C. Williams', 'S. Plath', 'E. Dickinson', 'A. Lorde', 'L. Hughes', 'W. Shakespeare', 'R. L. Schwartz', 'E. A. Poe']
print("\nThe first three poets in this list are:")
print(poets[:3])

print("\nThe middle three poets in this list are:")
print(poets[3:6])

print("\nThe last two poets in this list are:")
print(poets[6:])
