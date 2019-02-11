# -*- coding: utf-8 -*-
import random
answer = random.randint(0, 100)


while True:
    guess = int(input("What is your guess? "))

    if guess == answer:
        print("You guessed it! It is {0}".format(guess))
        break

    elif guess < answer:
        print("Your guess is too low!".format(guess))

    elif guess > answer:
        print("Your guess is too high!".format(guess))