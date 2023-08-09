PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    contents = names_file.readlines()  # returns content of file like a string

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for content in contents:
        stripped_name = content.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)


READLINES
REPLACE
STRIP