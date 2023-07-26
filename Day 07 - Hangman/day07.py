import random
import hangman_stages
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

print(hangman_stages.logo)

blanks = []
for letter in chosen_word:
    blanks += "_"

player_lives = 6

while blanks.count("_") != 0 and player_lives != 0:  # or while "_" not in blanks
    guessed_letter = input("Guess a letter: ")

    if guessed_letter in blanks:
        print("You have already guessed that letter")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter:
            blanks[position] = guessed_letter

    print(blanks)
    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(hangman_stages.stages[player_lives - 1])
        player_lives -= 1
        if player_lives == 0:
            print("You lose!")

    if "_" not in blanks:
        print("You win!")


