# Ted Paulo A. Feranil
# BSCPE 1-4

# Import pyfiglet module
import pyfiglet

# Create header
name = input("What's your name? ")
print(pyfiglet.figlet_format(f"Hello {name}! Welcome!", font="Ogre"))
print("=" * 45)
print("\033[34mDecrypt your text here!\033[0m")
print("_" * 45)

# Create a dictionary for characters
dict_char = {'*': 'a',
             '&': 'e',
             '#': 'i',
             '+': 'o',
             '!': 'u'}


# Substitute the character given by the user based on dictionary
def decryption(input_char):
    output_char = ""
    for symbol in input_char:
        if symbol in dict_char:
            output_char += dict_char[symbol]
        else:
            output_char += symbol
    print("\033[35mThe Plain Text:\033[0m", output_char, end='')


# Enter the text that user wants to decrypt
decryption(input("Enter a string to decrypt: "))

# Let the user continue the process or stop
while True:
    print()
    choice = input("\nDo you want to continue? Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
    if choice.upper() == "Y":
        decryption(input("Enter a string to decrypt: "))
    elif choice.upper() == "N":
        print("Exiting program bye!..." + "\U0001F600" + "\U0001F600")
        quit()
    else:
        choice = input("\nInvalid key, do you want to continue? Type \033[32mY\033[0m if yes "
                       "or \033[31mN\033[0m if no: ")
        if choice.upper() == "Y":
            decryption(input("Enter a string to decrypt: "))
        elif choice.upper() == "N":
            print("Exiting program bye!..." + "\U0001F600" + "\U0001F600")
            quit()
