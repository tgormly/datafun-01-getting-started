"""
Optional bonus. See course site for details.

Tim Gormly - 01/16/2023

This module simulates a game of Rock Paper Scissors using different animals.  The random module is imported so that the random.choice method can be used by the computer player to make their selection.  Nest if statements and the == operator are used to determine the winner of a round.  In these statements the .lower() method is used to account for user capitalization.

"""

import random

# Change the name below to a name of your choice

name = "The Gamemaster"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function
user_choice = input('Please enter your choice: wolf, eagle, or snake: \n')

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice.lower() == buddy_choice:
    print("We tied!")

if user_choice.lower() == 'wolf':
    if buddy_choice == 'eagle':
        print('Your wolf scares my eagle!\n~~You Win!~~\n')
    if buddy_choice == 'snake':
        print('My snake bites your wolf!\n~~You Lose!~~\n')

if user_choice.lower() == 'eagle':
    if buddy_choice == 'snake':
        print('Your eagle grabs my snake!\n~~You Win!~~\n')
    if buddy_choice == 'wolf':
        print('My wolf scares your eagle!\n~~You Lose!~~\n')


if user_choice.lower() == 'snake':
    if buddy_choice == 'wolf':
        print('Your snake bites my wolf!\n~~You Win!~~\n')
    if buddy_choice == 'eagle':
        print('My eagle grabs your snake!\n~~You Lose!~~\n')


# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""
PS C:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week 1\datafun-01-getting-started> & C:/Users/timgo/AppData/Local/Programs/Python/Python39/python.exe "c:/Users/timgo/OneDrive/Desktop/School/Spring2023/Week 1/datafun-01-getting-started/xtra_p1.py"

Hello, I'm The Gamemaster, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Please enter your choice: wolf, eagle, or snake:
eagle

You said eagle.
I said wolf.

My wolf scares your eagle!
~~You Lose!~~

PS C:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week 1\datafun-01-getting-started> & C:/Users/timgo/AppData/Local/Programs/Python/Python39/python.exe "c:/Users/timgo/OneDrive/Desktop/School/Spring2023/Week 1/datafun-01-getting-started/xtra_p1.py"

Hello, I'm The Gamemaster, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Please enter your choice: wolf, eagle, or snake:
snake

You said snake.
I said snake.

We tied!
PS C:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week 1\datafun-01-getting-started> & C:/Users/timgo/AppData/Local/Programs/Python/Python39/python.exe "c:/Users/timgo/OneDrive/Desktop/School/Spring2023/Week 1/datafun-01-getting-started/xtra_p1.py"

Hello, I'm The Gamemaster, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Please enter your choice: wolf, eagle, or snake:
eagle

You said eagle.
I said snake.

Your eagle grabs my snake!
~~You Win!~~
"""
