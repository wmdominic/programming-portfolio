name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#The function printed the name as a title.
#name is a variable and is in lowercase letters. title is a method and appears after the variable in the print() call.
#A method is an actionthat python can perform on a piece of data.
#The dot (.) after name tells Python to make the title method act on the variable name.
#Every method is followed by a set of parenthesis because methods often need additional information to do their work. (title method does not need additional information, so we leave the parenthesis empty.)

#title() method is often useful because you'll often want to think of a name as a piece of information.
#For example, you may want Ada, ADA, and ada to all be seen as the same name and display all of them as Ada.

#lower() method is particularly useful for storing data. Many times you won't want trust the capitalization that your users provide, so you'll want to convert strings to lowercase before storing them.

first_name = "william"
last_name = "lewandowski"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())


#f is for format. These are called f-strings because Python formats the string by replacing the name of any variable in braces with its value.

first_name = "jeremy"
last_name = "krovitz"
full_name = f"{first_name} {last_name}"
print(f"Hello, Mr. {full_name.title()}!")
message = f"My Boyfriend's name is: {full_name.upper()}."
print(message)

#f-strings can be used to compose a complete message (see above)

print("Python")
print("/tPython")
print("\tPython")
print("\t\tPython")

#\t adds a tab

print("Languages I am Studying:\nPython\nJavaScript\nCSS\nHTML")
print("Languages I am Studying:\n\tPython\n\tJavaScript\n\tCSS\n\tHTML")
print("Languages I am Studying:\t\nPython\t\nJavaScript\t\nCSS\t\nHTML")

#the last line of code didn't tab in because the code read to tab first then add a new line.