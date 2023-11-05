import random

while True:
    print("----------Welcome to RPS--------")

    # Variables to store scores
    user_score = 0
    comp_score = 0
    ties = 0

    name = input("Enter your name here: ")

    print("""Winning rules:
    1. Paper beats rock ---> Paper
    2. Rocks beats Scissors ---> Rock
    3. Scissors beats paper ---> Scissors""")

    # Variables created for choices
    print("""Choices are:
    1. Rock
    2. Paper
    3. Scissors""")

    # Enter your choice as an integer
    choice = int(input("Enter your choice from 1-3:"))
    print()  # Add a line space

    # Create a loop to get valid user input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input"))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("Your choice is", user_choice)
    print("Now it's the computer's turn")

    # Computer randomly chooses a number
    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print("The computer's choice is", comp_choice)

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"

    if ((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif ((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"
    elif user_choice == comp_choice:
        print("It's a Tie")
        result = "Tie"
    else:
        print("Scissors wins")
        result = "Scissors"

    # Declare a winner
    if result == "Tie":
        ties += 1
    elif result == user_choice:
        print("User wins")
        user_score += 1
    else:
        print("Computer wins")
        comp_score += 1

    # Display scores
    print("Scores are")
    print(name, "`s score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties are", ties)
#The Strip method is used to remove any leading or trailing whitespace,the lower method is used to convert the user's input to lowercase.
    repeat = input("Do you want to play again? (Yes/No): ").strip().lower()
    if repeat == "no":
        break
        print("Game Over!")
        Print("Thanks For playing")







