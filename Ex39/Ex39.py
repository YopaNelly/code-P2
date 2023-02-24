# Implement the Caesar cypher
import string
alphabet = string.ascii_lowercase  # a-z


def decrypt():
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    key = int(input("Enter key to decrypt: "))

    decrypted_message = ""

    for i in encrypted_message:

        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += i
    print("Your decrypted message is:\n", decrypted_message )



decrypt()
