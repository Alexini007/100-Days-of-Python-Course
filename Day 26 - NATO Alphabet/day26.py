import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
new_data = {row.letter: row.code for (index, row) in data.iterrows()}

should_continue = True
while should_continue:
    user_input = input("Type your message: \n").upper()
    try:
        final_list = [new_data[letter] for letter in user_input]
    except KeyError:
        print("Sorry, type only letters in the alphabet")
    else:
        should_continue = False
        print(final_list)
