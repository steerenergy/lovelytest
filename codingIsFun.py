# This is a Quick Test
# Shared var names: name = persons name, age = persons age


# Tom
# Create function that asks for users name and DOB year and prints age




# Nick
# Create function which gets the name of the persons favourite football team and tells them what you think of them
# When you tell them the opinion of the football team, address the person using the name they gave in the first part
# (it's polite y'know)




# John
# INTERPRET a 920,232 MB CSV file and plot this on a 4D Graph while figuring out the meaning of life
# Nah just kidding
# Create a function which calculates the circumference and area of a circle with the diameter being the age from part 1
import math
pi = math.pi
print("For no good reason, we're going to calculate some properties of a circle with a diameter equal to your age and devoid of units")


if age <= 0:
    print("I'm going to take the legal position that you're age zero, given you've not been born yet.")
    print("Which means there is no circle. End of.")
elif 0 < age:
    print("OK, here we go then ...")
    dia = age
    circ = pi * age
    area = pi / 4 * age ** 2
    print("A circle with a diameter equal to your age of ", age," has a circumference of",circ," and an area of ", area)
else:
    print("However, given you have an indecipherable age, we'll just go make a coffee ...")


