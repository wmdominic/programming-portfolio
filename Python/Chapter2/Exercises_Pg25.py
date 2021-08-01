#2-3. Personal Message

user_name = ("Philip")
print(f"Hello {user_name}, are you ready to learn some Python today?")

#Had a little difficulty. f goes outside the quotes, not near the {}. Noting special with the variable, just place it where it needs to be placed. Third try worked with some help with notes (not the book).

#We're going to try this again adding something a little more to it to challenge ourselves! :)

coding_languages = ("\n\tPython\n\tJavaScript\n\tCSS\n\tHTML")
print(f"The languages I am learning are:{coding_languages}")

#No errors! 

#2-4. Name Cases
your_name = ("beatrice")
print(your_name)
print(your_name.title())
print(your_name.upper())
print(your_name.lower())

#No Errors!

#2-5. Famous Quote

quote = ('"Hitch your wagon to a star."')
famous_person = ("Ralph Waldo Emerson")
message = (f"{famous_person} once said, {quote}")
print(message)

#No Errors First Try!!

#2-7. Stripping Names

someones_name = (" Meredith ")
lstrip = someones_name.lstrip()
rstrip = someones_name.rstrip()
strip = someones_name.strip()
print(f"The following is examples of no ws stripping, left ws stripping, right ws stripping, and both-side ws stripping:\n{someones_name}\n\t{lstrip}\t\t{rstrip}\n{strip}")
print(f"Let's make this more visible, even though the above experiment worked for me:\n{someones_name}\n{lstrip}\n{rstrip}\n{strip}")

#No Errors again
