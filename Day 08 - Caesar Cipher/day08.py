import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar_cipher(text, shift, direction):
    cipher_text = ""
    if direction == "decrypt":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position % 26]
        else:
            cipher_text += char
    print(f"This is your {direction}ed text: {cipher_text}\n")


should_continue = True
while should_continue:

    operation = input("Choose between 'encrypt' and 'decrypt'\n")
    if operation == "encrypt" or operation == "decrypt":
        message = input("Type your message here\n").lower()
        key = int(input("Type the key\n"))
    else:
        print("Wrong operation")
        operation = input("Choose between 'encrypt' and 'decrypt'\n")
        message = input("Type your message here\n").lower()
        key = int(input("Type the key\n"))
    caesar_cipher(message, key, operation)
    result = input("Type yes if you want to continue.\n")
    if result == "no":
        should_continue = False
