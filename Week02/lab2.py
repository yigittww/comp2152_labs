# Solution to Week 02 questions
import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: The Input should be an integer between 1 and 3!")
    # Determine the winner logic using if/elif/else
computerChoice = random.randint(1,3)

if playerChoice == computerChoice:
print("Tie")
