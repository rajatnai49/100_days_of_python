
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
chances = 6

print(logo3)
print("\nTo win, guess the word before the person hung. \n")

display = []
for _ in range(word_length):
    display += "_"
wrong_process = []

first_clue = random.randint(0, word_length-1)
second_clue = random.randint(0, word_length-1)

cnt = 0
for cnt in range(word_length):
    letter = chosen_word[cnt]
    if (cnt == first_clue or cnt == second_clue):
        display[cnt] = letter
    cnt += 1

print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess the letter:").lower()

    if guess in display:
        print(f"{guess} already in choosed. choose another one\n")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        chances -= 1
        if chances == 0:
            end_of_game = True
            print("You lose")
            print(f"The word was {chosen_word}")

    if not "_" in display:
        end_of_game = True
        print("You win!!")
        print(logo2)

    print(stages[chances])
