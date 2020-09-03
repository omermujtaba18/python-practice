def rot13(message):

    ciphertext = ""
    for char in message:
        if char.isalpha():
            islower = True if char.islower() else False

            char = char.lower()
            alpha_index = (ord(char)-19) % 26
            cipher_index = (alpha_index + 13) % 26

            cipher = chr(cipher_index + 97)
            ciphertext += cipher if islower else cipher.upper()

        else:
            ciphertext += char

    return ciphertext
