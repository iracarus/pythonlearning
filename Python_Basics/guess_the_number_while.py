# this is a guess the number game
import random

print('Hello. What is your name ?')
playerName = input()

number = random.randint(1,20)

print('Well, ' + playerName + ', I am thinking of a number between 1 and 20.')

currentGuess = None
trials = 0
while currentGuess != number:
    print('Take a guess.')
    currentGuess = input()

    if int(currentGuess) > number:
        print('Your guess is too high.')
    elif int(currentGuess) < number:
        print('Your guess is too low.')
    elif
        break   # This condition is the correct guess

    trials = trials + 1

print('Good Job. ' + playerName + '. You guessed the number in ' + str(trials) + ' guesses.')
