# Ted Paulo Feranil
# BSCPE 1-4

# Print header
name = input("Enter your name: ")
print("\033[36mThe Vigenère Cipher\033[0m".center(59, "="))
print(f"Good day {name}\U0001F929, encrypt your message here!\U0001F447")
print("-" * 50)


# Create a program that will encrypt given text through Vigenère Cipher
def cipher(message, key):
    # Create dictionary
    dict_char = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                 'X': 23, 'Y': 24, 'Z': 25}

    # Gather the number per letter based on dictionary for key and message
    ciphertext = []
    for a, b in enumerate(message):
        message_number = dict_char[b]
        key_number = dict_char[key[a % len(key)]]
        add = (message_number + key_number) % 26
        ciphertext.append(add)

    # Convert the gathered numbers into string
    ciphertext = ''.join([list(dict_char.keys())[list(dict_char.values()).index(i)] for i in ciphertext])
    print(f"\nSuccessful! \U0001F973 \n\033[33mHey {name}, here's the ciphertext:\033[0m", ciphertext)


# Input it in uppercase
cipher(input("Enter the message: ").upper().replace(" ", ""),
       input("Enter the key: ").upper().replace(" ", ""))

# Let the user continue the process or stop
while True:
    choice = input("\nDo you want to continue? Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
    if choice.upper() == "Y":
        cipher(input("Enter the message: ").upper(), input("Enter the key: ").upper())
    elif choice.upper() == "N":
        print("Exiting program\U0001F44B...")
        quit()
    else:
        choice = input("\nInvalid key, do you want to continue? Type \033[32mY\033[0m if yes "
                       "or \033[31mN\033[0m if no: ")
        if choice.upper() == "Y":
            cipher(input("Enter the message: ").upper(), input("Enter the key: ").upper())
        elif choice.upper() == "N":
            print("Exiting program\U0001F44B...")
            quit()