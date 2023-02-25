from art import logo
import random
import click


def guess_number():
    click.clear()
    guess = random.randint(1, 100)
    print(logo)
    difficulty = input("Choose a difficulty. from 'easy', 'medium' or 'hard: ")
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'easy':
        guesses = 8
    elif difficulty == 'hard':
        guesses = 5

    while guesses > 0:
        if guesses > 1:
            print(
                f"\nYou have {guesses} guesses left for the number that I'm thinking")
        else:
            print(f"\nLast try is remaining")
        attempt = int(input("\nGuess the number: "))
        if attempt == guess:
            print(
                f"\nCorrect! The answer was {guess}. Thanks for completing that! 😁")
            break
        elif attempt > guess:
            print("\nToo High.")
        elif attempt < guess:
            print("\nToo Low.")
        guesses -= 1

    if guesses == 0:
        print("\nGame over.")

    play_again = input("\nDo you want to play again y/n?: ")
    if play_again == 'y':
        click.clear()
        guess_number()
    else:
        print("Sayonara!!")


guess_number()
