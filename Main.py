import random

print("Welcome to the number guessing game")

play_again = "Y"

while play_again.upper() == "Y": # The Loop so people can continue playing when they enter a wrong number
    number = random.randint(1, 100)
    guess = None
    tries = 0

    print("Guess a number between 1 and a 100")

    while guess != number: # Loop till number gets guessed
        guess = input("Take a guess: ")
        guess = int(guess)
        tries = tries + 1

        if guess < number: # stuff below is pretty much self explanatory
            print("Higher")
        elif guess > number:
            print("Lower")
        elif guess == number:
            print("Congrats you guessed it in ", tries, "tries")
        else:
            print("Incorrect input, guess a number between 1-100") 


    while True: # Keeps asking the user if they want to play again. If they enter anything else than Y or N the program will keep asking until the user gives a valid input
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Wrong input")
