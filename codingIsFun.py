# This is a Quick Test
# Shared var names: name = persons name, age = persons age


# Tom

# Create function that asks for users name and DOB year and prints name and age
# User Input
name = input("What is your name? ")
# Get date is an integer
dob = int(input("Enter the Year you were Born? (Honesty IS essential ;)) "))
age = 2018-dob
# Print Information
print("Hello {}, your are approx {} years old.\n".format(name, age))

# Make comment on their age
if age <= 0:
    print("Wow. You were born in the future. Good Job. Please teach me your ways")
elif 0 <= age < 5:
    print("You're way too young - WHO are you and WHY are you doing this?!")
elif 5 <= age < 15:
    print("Shouldn't you be at school right now? Get back to work")
elif 15 <= age < 18:
    print("Nah mate you're lying. Get real")
elif 18 <= age < 25:
    print("Wow - someones 'mature'")
elif 25 <= age < 35:
    print("Hi Cory - Hope you're doing well. Again - if you're not Cory STOP LYING")
elif 35 <= age < 40:
    print("Good Job - you've made it far *Cries Emotionally*")
elif 40 <= age < 50:
    print("How's the mid-life crisis going? Hope you'v enjoyed taking up golf")
elif 50 <= age < 60:
    print("To be honest, you're getting old now - probably should think about retiring.")
elif 60 <= age < 80:
    print("Wow! You really are old?! I'm surprised you even managed to put your date of birth in correctly")
elif 80 <= age < 100:
    print("Obviously Lying. Stop. It's not big and it's not clever")
elif 100 <= age < 150:
    print("What bit of 'lying' do you not understand?! \nGet OUT.")
elif 150 <= age < 200:
    print("You don't exist. You are FAKE NEWS")
elif age >= 200:
    print("Nick Ryan - Stop messing around and get back to work")
else:
    print("Well this is awkward... You must have done something fairly stupid to get this message to come up."
          "\nEither you don't know how old you are or you need an eye test.")


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
# Create a function which calculates the circumference and area of a circle with the diameter being the age from part 1
import math
import time

pi = math.pi
print("For no good reason, we're going to calculate some properties of a circle with a diameter equal to your age"
          "\n ... and devoid of units.")
time.sleep(2)
print("Let the electrons get up to speed ...")
time.sleep(2)
print("... mmm ... mmm ... difficult ... bit of a sorting hat moment ...")
time.sleep(2)

if age <= 0:
    print("I'm going to take the legal position that you're age zero, given you've not been born yet.")
    time.sleep(1)
    print("Which means there is no circle. End of.")
elif 0 < age:
    print("OK, here we go then ...")
    time.sleep(1)
    dia = age
    circ = pi * age
    area = pi / 4 * age ** 2
    print("A circle with a diameter equal to your age of ", age," has a circumference of",circ," and an area of ", area)
    time.sleep(2)
    print("Go and make a coffee and calm down after all that excitement")
else:
    print("However, given you have an indecipherable age, we'll just go make a coffee ... numpty")


