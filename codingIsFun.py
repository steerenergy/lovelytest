# This is a Quick Test
# Shared var names: name = persons name, age = persons age


# Tom
# Create function that asks for users name and DOB year and prints age




# Nick
# Create function which gets the name of the persons favourite football team and tells them what you think of them
# When you tell them the opinion of the football team, address the person using the name they gave in the first part
# (it's polite y'know)




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


