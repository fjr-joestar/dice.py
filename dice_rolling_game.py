# Loop (Repetition so the user continues)
# Ask: roll the dice?
# If user enter y
#   Generate two random numbers
#   Print them
# If user enters n
#   Print thank you message
#   Terminate
# Else,
#   Print invalid choice
import random

while True: # This line creates the loop

    choice = input ("Greetings, Guardian. Would you like to roll the Dice? (y/n):").lower()
    if choice == "y":
        die1 = random.randint(1, 32)
        die2 = random.randint(1, 32)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Farewell, Guardian.")
        break # This line ends the loop
    else:
        print("That choice is invalid, Guardian")
    
