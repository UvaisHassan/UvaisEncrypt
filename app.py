import crypto

options = [
    "Encryption - E",
    "Decryption - D",
    "\nExit - X"
]

for x in options:
    print(x)

choice = ""
temp = ""
flag = 0

while choice.upper() != "X":
    choice = input("\n\nEnter your choice: ")

    if choice.upper() == "X":
        continue

    elif choice.upper() == "E":
        flag = 1
        temp = crypto.encrypt()
        print("Encrypted message is " + temp)

    elif choice.upper() == "D":
        if flag == 0:
            print("You haven't encrypted anything yet!!!")
            continue
        print("Decrypted message is " + crypto.decrypt(temp))

    else:
        print("Invalid choice!!!")

print("\nExiting the program!")
