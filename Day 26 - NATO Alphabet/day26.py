import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
new_data = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Type your message: \n")
user_list_of_letters = [letter.upper() for letter in user_input]

final_list = [new_data[letter] for letter in user_list_of_letters]
print(final_list)
