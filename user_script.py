"""
Tim Gormly - 01/16/2023

My Domain this semester is hockey.

This script will compare the total number of goals scored by three different players in a season.

This script will demonstrate my ability to use these built-in functions: input(), print(), type(), int(), float(), min(), max(), assign variables, and communicate with the user (using print()) and in code (using comments)
"""
import webbrowser


print("""Tim Gormly, Project 1.
Hockey Goal Statistics\n""")

### 
# Part 1
# get 3 players' total goals scored in a season using the input() function
###

print("Let's compare the total goals scored of three different players this season\n")

#gather input from user, and change input to int type
score1 = input("How many goals did the first player score? ")
score1 = int(score1)

# give the user feedback depending on the number of goals scored
if(score1 == 1):
    print(f"Only {score1} goal?  That's a bad season")

if(score1 < 10 and score1 > 1):
    print(f"Only {score1} goals?  That's a bad season")

if(score1 > 9 and score1 < 40):
    print(f"{score1} goals is an OK season")

if(score1 > 40):
    print(f"{score1} goals!?  That's a great season!")

score2 = input("How many goals did the second player score? ")
score2 = int(score2)

# give the user feedback depending on the number of goals scored
if(score2 == 1):
    print(f"Only {score2} goal?  That's a bad season")

if(score2 < 10 and score2 > 1):
    print(f"Only {score2} goals?  That's a bad season")

if(score2 > 9 and score2 < 40):
    print(f"{score2} goals is an OK season")

if(score2 > 40):
    print(f"{score2} goals!?  That's a great season!")


score3 = input("How many goals did the third player score? ")
score3 = int(score3)

# give the user feedback depending on the number of goals scored
if(score3 == 1):
    print(f"Only {score3} goal?  That's a bad season")

if(score3 < 10 and score3 > 1):
    print(f"Only {score1} goals?  That's a bad season")

if(score3 > 9 and score3 < 40):
    print(f"{score3} goals is an OK season")

if(score3 > 40):
    print(f"{score3} goals!?  That's a great season!")


print("Thank you!\n")
print("Computing input data...")
print(".")
print(".")
print(".")


if(type(score3) is int):
    print("Success!\n\nLet's review your data:\n")

###
# Part 2
# Show information about these players' season
###

divider = "----------------------------------------"
print(divider)

# show the total of all goals scored, the sum of all goals scored
total_goals = score1 + score2 + score3
print(f"Total Goals Scored: {total_goals}")
print(divider)

# show the average of all goals scored
average_goals = total_goals / 3
print(f"Average Number of Goals Scored: {round(average_goals, 3)}")
print(divider)

# show the product of all goals scored
product_of_goals = score1 * score2 * score3
print(f"Product of Goals Scored: {product_of_goals}")
print(divider)

# show the smallest number of goals scored
fewest_goals = min(score1, score2, score3)
print(f"Fewest Goals Scored: {fewest_goals}")
print(divider)

# show the largest number of goals scored
most_goals = max(score1, score2, score3)
print(f"Most Goals Scored: {most_goals}")
print(divider)

# show the range of goals scored
print(f"The total number of goals scored ranges between {fewest_goals} and {most_goals}")
print(divider)



# ask user if they would like to see additional statistics

moreStatsChoice = input("Would you like to see more statistics on the web? (y/n)\n")

if(moreStatsChoice.lower() == "y"):
    webbrowser.open_new("https://www.hockey-reference.com/")

print("\nThank you!  Good-bye\n")
