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
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def name_validation(self):
        q = input(f"Is {self.name} correct? (Y/N) ")
        if q == "N":
            self.name = input("What's your name? ")
            self.name_validation()
        elif q == 'Y':
            pass
        else:
            print("Sorry, I did not understand you...")
            self.name_validation()

class Cat():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def name_validation(self):
        q = input(f"Is {self.name} correct? (Y/N) ")
        if q == "N":
            self.name = input("What's your cat's name? ")
            self.name_validation()
        elif q == 'Y':
            pass
        else:
            print("Sorry, I did not understand you...")
            self.name_validation()


# Game starts

user = User(name = input("What's your name? "))
user.name_validation()

print(f"Good morning {user.name} and welcome to Catnip!")

user_cat = Cat(name = input("What's your cat's name? "))
user_cat.name_validation()




