'''
This module is used to implement a simple guessing game
'''

from curses.ascii import isdigit
from random import randint

GAME = "GUESSING GAME CHALLENGE"
PLAY = 'Y'
print(f"{GAME:^175}\n")
print("The aim of this game is to guess the randomly generated number within the range of 1 to 100")
print("The game will provide the following hints as to narrow down your guesses:")
print("\t> On a player's first turn, if their guess is within 10 of the number, the game will say WARM! Otherwise it will say COLD!")
print("\t> On all subsequent turns, if a guess is closer to the number than the previous guess, the game will say WARMER! Otherwise it will say COLDER!")
print("At the end of every turn, the player could choose to continue guessing or exit the game by entering 'stop'")
print("At the end of the game, the number of guesses taken will be revealed!")
print("You may wish to continue the game how many ever times you would like to!!!\n")
while PLAY == 'Y':
    correctNumber = randint(1,100)
    guesses = []
    INVALID_INPUT = True
    while INVALID_INPUT:
        entry = input("Enter your guess: ")
        if entry == 'stop':
            break
        if not entry.isdigit():
            print("Invalid Entry")
            continue
        guess = int(entry)
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS!")
            continue
        INVALID_INPUT = False
    if entry == 'stop':
        break
    guesses.append(guess)
    if guess == correctNumber:
        print("CORRECT GUESS!")
        print(f"The number of valid guesses that you took was: {len(guesses)} {guesses}")
        print(f"The correct number is: {correctNumber}")
        PLAY = input("Do you want to play again (Y/N)? ")
        continue
    if abs(guess - correctNumber) <= 10:
        print("WARM!")
    else:
        print("COLD!")
    while entry != 'stop':
        previous = guess
        INVALID_INPUT = True
        while INVALID_INPUT:
            entry = input("Enter your guess: ")
            if entry == 'stop':
                break
            if not entry.isdigit():
                print("Invalid Entry")
                continue
            guess = int(entry)
            if guess < 1 or guess > 100:
                print("OUT OF BOUNDS!")
                continue
            INVALID_INPUT = False
        if entry == 'stop':
            break
        guesses.append(guess)
        if guess == correctNumber:
            print("CORRECT GUESS!")
            print(f"The number of valid guesses that you took was: {len(guesses)}")
            print(f"The correct number is: {correctNumber}")
            PLAY = input("Do you want to play again (Y/N)? ")
            break
        if abs(guess - correctNumber) < abs(previous - correctNumber):
            print("WARMER!")
        else:
            print("COLDER!")
    if entry == 'stop':
        print("You have chosen to leave the game :/")
        print(f"The number of valid guesses that you took was: {len(guesses)}")
        print(f"The correct number is: {correctNumber}")
        print("Game Over!")
        break
print("Thank You for playing!")
