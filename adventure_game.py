import time
import random

# Main variables for scoring, number of turns and if user wants to play again
score = 10
turns = 0
play = "y"

# Function for waiting before printing
def print_pause(n):
    print(n)
    time.sleep(0)

# Function for checking if input in game functions that require int is correct
def get_int(message):
    x = input(message)
    while not x.isdigit():
        print_pause("Please enter an integer.")
        x = input(message)
    return int(x)

# Function for generating easy question
def easy():
    global turns,score
    turns += 1
    x = random.randint(1,10)
    y = random.randint(1,10)
    correct = x * y
    answer = get_int(f"what is {x} * {y} ? ")
    if answer == correct:
        print_pause("Correct answer :)")
        score += 1
        print_pause(f"Your score now is {score}.")
        print_pause(f"You can solve more {10 - turns} questions.")
    else:
        print_pause("Wrong answer! :(")
        score -= 1
        print_pause(f"Your score now is {score}.")
        if score < 20 and score > 0:
            print_pause(f"You can solve more {10 - turns} questions.")

# Function for generating normal question
def normal():
    global turns,score
    turns += 1
    x = random.randint(11,19)
    y = random.randint(11,19)
    correct = x * y
    answer = get_int(f"what is {x} * {y} ? ")
    if answer == correct:
        print_pause("Correct answer :)")
        score += 3
        print_pause(f"Your score now is {score}.")
        if score < 20 and score > 0:
            print_pause(f"You can solve more {10 - turns} questions.")
    else:
        print_pause("Wrong answer! :(")
        score -= 1
        print_pause(f"Your score now is {score}.")
        print_pause(f"You can solve more {10 - turns} questions.")

# Function for generating hard question
def hard():
    global turns,score
    turns += 1
    x = random.randint(11,19)
    y = random.randint(21,29)
    correct = x * y
    answer = get_int(f"what is {x} * {y} ? ")
    if answer == correct:
        print_pause("Correct answer :)")
        score += 5
        print_pause(f"Your score now is {score}.")
        if score < 20:
            print_pause(f"You can solve more {10 - turns} questions.")
    else:
        print_pause("Wrong answer! :(")
        score -= 1
        print_pause(f"Your score now is {score}.")
        if score < 20 and score > 0:
            print_pause(f"You can solve more {10 - turns} questions.")

# Function for operating the game
def game():
    global play,score,turns
    score = 10
    turns = 0
    print_pause("You are kidnapped by a mad Mathematecian.")
    print_pause("You should solve some math questions to go home.")
    print_pause("You are not supposed to use a calculator!")
    print_pause("Every easy question will give you 1 point.")
    print_pause("Every normal question will give you 3 point.")
    print_pause("Every hard question will give you 5 point.")
    print_pause("Every wrong answer will make you lose 1 point")
    print_pause("You start with 10 points and your goal is to have 20 points.")
    s = "You must reach the 20 points by solving less than 11 problems."
    print_pause(s)
    while turns < 11 and 0 < score < 20 :
        print_pause("Enter 1 to solve easy question")
        print_pause("Enter 2 to solve normal question")
        print_pause("Enter 3 to solve hard question")
        print_pause("What do you like to do?")
        choice = input("Please enter 1 or 2 or 3: ")

        while choice != "1" and choice != "2" and choice != "3":
            choice = input("Please enter 1 or 2 or 3: ")

        if choice == "1":
            easy()
        elif choice == "2":
            normal()
        else:
            hard()

    if score >= 20:
        print_pause("Congratulations! You won :)")
    else:
        print_pause("Unfortunately you have lost :(")
    x = input("Do you want to play again? (y/n): ")
    while x != "y" and x != "n":
        print_pause("Please enter a valid input. ")
        x = input("Do you want to play again? (y/n): ")
    play = x
while play == "y":
    game()