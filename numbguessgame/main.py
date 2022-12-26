from art import logo
import random
import os

def game(tries, number):
    guess = -1
    while tries > 0 and guess != number:
        guess = int(input("Make a guess: "))
        if guess > number:
            tries -=1
            print(f"Too high. Guess Again.\nYou have {tries} attempts remaining to guess the number.")
        elif guess < number:
            tries -=1
            print(f"Too low. Guess Again.\nYou have {tries} attempts remaining to guess the number.")
        else:
            print(f"You got it!. The answer was {guess}.")
    
    if tries == 0:
        print(f"You ran out of tries. The number was {number}.")


cont = True
while cont:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while 1: 
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
        if(difficulty == "easy"):
            tries = 10
            break
        elif difficulty == "hard":
            tries = 5
            break
        else: 
            print("Invalid Input.")

    print(f"You have {tries} attempts to guess the number.")

    number = random.randint(1, 100)

    game(tries, number)
    while 1: 
        still_play = input("Do you want to play again? 'yes' or 'no'?: ").lower()
        if still_play == "no":
            cont = False
            os.system('clear')
            break
        if still_play == "yes":
            os.system('clear')
            break
        elif still_play != "yes":
            print("Invalid Input.")
