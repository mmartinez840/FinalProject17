# I imported time in order to use the "type_out" function.
import sys, time

# This function will change how fast some of the strings are typed out.
def type_out(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
# This sets the speed of the typing out of the strings to 0.02.
        time.sleep(0.02)

# The player's answer to first string will be put through this function. If the player's response is "yes," then they will be asked to make a choice.
def pathway1():
# This allows for the player to enter an input.
    response1 = input().lower()
    if response1 == "yes":
# The player is asked to enter either '1' or '2' to select their answer.
        print("""You awaken suddenly to the sound of strange ambient echos.
As you open your eyes and look around you, you find yourself in a strange tunnel with flesh-like walls.
You begin to notice a familiar darkness and coldness.
Your sight is obscured by an omnipresent fog that seems to encase all surroundings within five feet of you.
As you begin to explore the mysterious area, you also notice a number of odd, plant-like growths.
They appear to be writhing and covered in a slimy substance.
As you are walking along the bizzare path, you see a red-headed teenager, visibly injured.
It's Barb! Do you (1)help her or (2)protect yourself and continue to move along? """)
    elif response1 == "no":
        print("Wow, that's kind of rude.")
# If the player does not answer "yes" or "no" they will get this message.
    else:
        print("It's a 'yes' or 'no' question...")

# This function while take an input for the question asked in pathway1. It will return a string based on the player's answer.
def pathway2():
    response2 = input().lower()
    if response2 == "1":
# I formatted the strings using triple quotes to make them easier to read and also easier to edit.
        print("""Yikes! It turns out Barb had been attacked by some sort of Upside Down creature and subsequently became infected with a deadly disease.
By helping her, you became infected, as well. You died!""")
    elif response2 == "2":
        print("""Yikes! It turns out Barb had been attacked by some sort of Upside Down creature and subsequently became infected with a deadly disease.
You dodged a bullet by moving on and leaving her alone. As you walk through the pulsing tunnels, you begin to notice even more plant-like creatures.
You specifically notice hissing tendrils moving and wrapping around the tunnel walls. Suddenly, you trip over a tendril and become tangled.
The tendril begins to tightly wrap around you. You must fight your way out. Do you try to (1)wrestle your way out of it's grasp or (2)punch it? """)
# If the player does enter '1' or '2' they will get this message.
    else:
        print("Type '1' or '2' to make a decision.")

# This function while take an input for the question asked in pathway2. It will return a string based on the player's answer.
def pathway3():
    response3 = input().lower()
    if response3 == '1':
        print("The more you wrestled with the tendril, the tighter it wrapped around you. You suffocated and died. :( ")
    elif response3 == '2':
        print("""Wow, you must be really strong!! You punched the tendril really hard and were able to get out of it's grasp.
You continue walking through the Upside Down. You hear faint footsteps behind you.
You look back and find yourself being followed by a creature that resembles a crossover of an amphibian and a reptile.
The creature is not much larger than a cat and has a mouth that resembles the petals of a flower. It's a Demodog!
You know that although Demodogs can be friendly and helpful, they are carnivorous, and can kill you in an instant.
Do you (1)try to befriend the Demodog or (2)try to kill it? """)
    else:
        print("Type '1' or '2' to make a decision.")

# This function while take an input for the question asked in pathway3. It will return a string based on the player's answer.
def pathway4():
    response4 = input().lower()
    if response4 == "1":
        print("""Good decision! The Demodog clearly likes you and begins to trust you.
You keep travelling through the tunnel, now with your Demodog companion.
You start to become homesick and tired of the intensity of the Upside Down. It's dark and cold and you're starving.
You desperately need energy in order to survive. Do you (1)eat the Demodog or (2)scavenge for other possible foods? """)
    elif response4 == "2":
        print("You are no match for the Demodog and are killed instantly. Woops! ")
    else:
        print("Type '1' or '2' to make a decision.")

# This function while take an input for the question asked in pathway4. It will return a string based on the player's answer.
def pathway5():
    response5 = input().lower()
    if response5 == "1":
        print("Your plan to betray the trustworthy Demodog backfired. The demodog fights back and kills you instantly. You died! ")
    elif response5 == "2":
        print("""You scavenge the tunnels for food. You find nothing.
The only possible source of food you can think of are the tendrils, however, you refuse to get close to one those, again.
Luckily, you remember about the crackers you had in your pocket before waking up in the Upside Down. Heck yea.
As you are eating your crackers, you suddenly hear a loud rumble. The fleshy walls of the tunnel begin to shake. The tendrils retract against the wall.
In the distance you see a Demogorgan surrounded by fog. You accidentally make eye contact with it and it begins to run toward you.
Oh no! Do you (1)run away or (2)try to fight it? """)
    else:
        print("Type '1' or '2' to make a decision.")

# This function while take an input for the question asked in pathway5. It will return a string based on the player's answer.
def pathway6():
    response6 = input().lower()
    if response6 == "1":
        print("""You run as fast as you can, knowing that you are no match for the Demogorgan.
You make a sharp turn to throw the Demogorgan off and you end up coming across a literal wound in the fabric of space and time.
You hurrily crawl through it. Suddenly, you find yourself back in Hawkins, Indiana. Good job, you escaped the Upside Down! """)
    elif response6 == "2":
        print("You were absolutely no match for the Demogorgan. It literally ripped you to shreds in seconds. Good try, though!  ")
    else:
        print("Type '1' or '2' to make a decision.")

# class MyClass(object):
#     def __init__

# This string introduces the game. It asks the player a "yes" or "no" question. The input to said question will be taken in the pathway1 function.
# I used "type_out" instead of "print" to use the "type_out" function for this particular string.
type_out("""Welcome to Strangers Things: The Text Based Game.
The goal of this game is to escape the Upside Down ALIVE!
You will have to make the correct choices throughout the game in order to succeed.
One you make a choice, you cannot go back, so choose wisely. Would you like to begin the game? Type 'yes' or 'no' """)

# This will call all the functions.
pathway1()
pathway2()
pathway3()
pathway4()
pathway5()
pathway6()

