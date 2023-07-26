import random
import hangman_stages
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

print(hangman_stages.logo)

display = []
for letter in chosen_word:
    display += "_"

player_lives = 6

while display.count("_") != 0 and player_lives != 0:  # or while "_" not in display
    guessed_letter = input("Guess a letter: ")

    if guessed_letter in display:
        print("You have already guessed that letter")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter:
            display[position] = guessed_letter

    print(display)
    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(hangman_stages.stages[player_lives - 1])
        player_lives -= 1
        if player_lives == 0:
            print("You lose!")

    if "_" not in display:
        print("You win!")


