# Hi! This is the code for my first Python project. 
# The main idea is to develop a mini-game 
# in which you cat take care of your cat

import time

# Greetings
"""
print("Hello! Welcome to Catnip")
time.sleep(1)

message = "Loading game..."
for letter in message:
    print(letter, " ", end="", flush = True)
    time.sleep(0.5)

print("Hooray! Game loaded correctly")

"""

# Initial settings

cat_name = input("What's your cat's name? " )
    
def name_validation(name):
    q = input(f"Is {name} correct? (Y/N) ")
    if q == "N":
        name = input("What's your cat's name? " )
        name_validation(name)
    elif q == 'Y':
        pass
    else:
        print("Sorry, I did not understand you...")
        name_validation(name)

name_validation(cat_name)
