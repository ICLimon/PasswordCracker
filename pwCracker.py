import hashlib
import random
import string

pwGuess = ""
guess = ""
passwordFile = "passList.txt"

attack = input("Select attack: Dictionary  |  Brute     ")
mode = input("Select mode: SHA-256  |  MD5  |  Text     ")

password = input("What is the password? ")

# Translates password to MD5 hash
def md5Password(password):
    encodedMd5Password = password.encode("utf-8")
    return(hashlib.md5(encodedMd5Password.rstrip()).hexdigest())

# Trandlates password to SHA-256 hash
def shaPassword(password):
    encodedSha256Password = password.encode("utf-8")
    return(hashlib.sha256(encodedSha256Password.rstrip()).hexdigest())

# Gets random word
def bruteForce():
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k = len(password)))
        return guess

count = 0

# Dictionary attack to according mode and prints attempts
if(attack == "Dictionary"):
    passwordFile = open(passwordFile)
    for word in passwordFile:
        if(mode == "MD5"):
            guess = md5Password(word)
            pwGuess = md5Password(password)
        elif(mode == "SHA-256"):
            guess = shaPassword(word)
            pwGuess = shaPassword(password)
        elif(mode == "Text"):
            guess = word.rstrip()
            pwGuess = password.rstrip()
        
        count = count + 1
        if(guess == pwGuess):
            print("\n")
            print(f"Attempts: {count}")
            print("\n")
            print("Password: " + pwGuess.rstrip())
            quit()
    print("Password not found")

# Brute force attack according to mode and prints attempts
if(attack == "Brute"):
    print("Cracking Password...")
    while True:
        randomWord = bruteForce()
        if(mode == "MD5"):
            pwGuess = md5Password(password)
            guess = md5Password(randomWord)
        elif(mode == "SHA-256"):
            pwGuess = shaPassword(password)
            guess = shaPassword(randomWord)
        elif(mode == "Text"):
            pwGuess = password.rstrip()
            guess = randomWord.rstrip()
            
        count = count + 1
        print("-----" + str(randomWord) + "-----")
        if(attempts > 100000):
            print("Password not found")
            quit()
        if(guess == pwGuess):
            print(f"Attempts : {count}")
            print("Password: " + guess)
            quit()
