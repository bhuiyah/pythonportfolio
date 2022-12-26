from art import logo, vs
from game_data import data
import random
from os import system

def game():
    score = 0
    print(logo)
    person1 = random.choice(data)
    
    still_playing = True
    while still_playing:
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        person2 = random.choice(data)
        while person2 == person1:
            person2 = random.choice(data)

        print(vs)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")

        if person1['follower_count'] > person2['follower_count']:
            correctAnswer = "a"
        else:
            correctAnswer = "b"

        while 1:
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if choice == correctAnswer:
                system('clear')
                print(logo)
                score+=1
                print(f"You're right!. Correct score = {score}.")
                person1 = person2
                break
            elif choice != correctAnswer and (choice == "a" or choice == "b"):
                system('clear')
                print(logo)
                print(f"Sorry, that's wrong. Final Score: {score}.")
                still_playing = False
                break
            else:
                "Invalid Input"

again = True
while again:
    game()
    while 1:
        still = input("Do you want to play again? 'yes' or 'no': ").lower()
        if still == "no":
            again = False
            break
        elif still == "yes":
            break
        else:
            print("Invalid Input")
        
    system('clear')
