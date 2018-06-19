# This is a Quick Test
# Shared var names: name = persons name, age = persons age


# Tom
# Create function that asks for users name and DIB year and prints age

# add in name for toms bit
name = input("What is your name? ")


# Nick
# Create function which gets the name of the persons favourite football team and tells them what you think of them
# When you tell them the opinion of the football team, address the person using the name they gave in the first part
# (it's polite y'know)

# Introduce yourself
print("Hey {}, \n".format(name))
# Ask for favourite footy team
foot_name = input("Please type in the name of your favourite football team ")
# print first response
print("What {}, really?\n".format(foot_name))
print("Honestly,", foot_name, "... let me think")
# print length of string count
print(foot_name, "has", len(foot_name), "letters in it.")
# convert to lower case
# foot_name = foot_name.lower()
# comment on their choice of team
if foot_name.lower() == "formby squirrels":
    print("Great Choice {} good old {} are my fave too".format(name, foot_name))
else:
    print("Looser, looser", name, "is a looser", foot_name, "are pants!")

# John
# Interpret a 920,232 MB CSV file and plot this on a 4D Graph while figuring out the meaning of life
# Nah just kidding
# Create a function which calculates the circumference and area of a circle with the diameter being the age from part 1
