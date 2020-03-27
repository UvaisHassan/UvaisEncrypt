def encrypt():

    msg_to_encrypt = input("Enter your secret message: ")
    encrypt_key = input("Enter encryption key: ")

    message = ""

    i = 0
    for letter in msg_to_encrypt:
        message = message + chr(ord(letter) + ord(encrypt_key[i]))
        i += 1
        if i == len(encrypt_key):
            i = 0

    return message


def decrypt(temp):

    msg_to_decrypt = input("Enter encrypted message (or Enter COPY to use the encrypted message from above): ")
    if msg_to_decrypt.upper() == "COPY":
        msg_to_decrypt = temp

    decrypt_key = input("Enter decryption key: ")

    message = ""

    i = 0
    for letter in msg_to_decrypt:
        message = message + chr(ord(letter) - ord(decrypt_key[i]))
        i += 1
        if i == len(decrypt_key):
            i = 0

    return message
