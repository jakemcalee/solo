import random
import string


print("Password Generator")
print("===================")

print("\n")

passLength = int(input("Enter How Long You Want Your Password: "))
useLetters = input("Include Letters? (y/n)").lower()
useNumbers = input("Include Numbers? (y/n)").lower()
useSymbols = input("Include Symbols? (y/n)").lower()

char = ""

if useLetters == "y":
    char += string.ascii_letters
if useNumbers == "y":
    char += string.digits
if useSymbols == "y":
    char += string.punctuation


if char == "":
    print("You have to choose a character type.")
else:
    password = "".join(random.choice(char) for _ in range(passLength))
    print("================================")
    print("Generated Password: ", password)

