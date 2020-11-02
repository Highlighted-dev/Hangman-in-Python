from random import randint

# Getting random word from list
words = ["apple", 'carrot', 'strawberry', 'blueberry', 'banana', 'orange', 'pineapple', 'cherry', 'grapefruit',
         'lemon', 'mango', 'pear', 'raspberry', 'watermelon']
word = words[randint(0, len(words) - 1)]

# Changing letters to "_", so player will be able to see the length of the word, but not actually the word.
hangmanWord = "_" * len(word)


# With this function program will draw a part of stickman. Higher number (more mistakes) = more parts
def draw_hangman(i,word):
    return {
        0: 'Hangman:\n ',
        1: 'Hangman:\n o \n',
        2: 'Hangman:\n o \n | \n',
        3: 'Hangman:\n o \n-| \n',
        4: 'Hangman:\n o \n-|- \n',
        5: 'Hangman:\n o \n-|-\n/ \n',
        6: 'Hangman:\n o \n-|-\n/ \\ \n',
        7: f'Hangman:\n x \n-|-\n/ \\ \nYou lost :(. The word was "{word}"'
    }[i]


# Creating two variables: numberOfMistakes will display us how many wrong letter have been entered,
# playerLetters will display the letters that player entered
numberOfMistakes = 0
playerLetters = ['']

# Our main loop: 1. The program will check if there's any "_" in the word - if not, that means that player won.
# 2. We are changing variable type to list so program will be able to change letters in word
# 3. The program will display letters that player have entered. Next the program will ask to enter a letter
# 4. If player have entered the letter before, program will display the text "You entered that letter before!"...
#  ... otherwise the program will add this letter to a list named playerLetters
# 5. The program will check if the letter that player have entered is in the word. If no - program will add 1 to...
# ... number of mistakes. Otherwise the program will change the "_" in hangmanWord to a letter
# 6. The function draw_hangman will draw a hangman that depends of numberOfMistakes.
# 7. And now we will change back the hangmanWord variable from list to string.
while True:
    if "_" in list(hangmanWord):
        print(hangmanWord)
    else:
        print(f"Congratulations, you won! The word was {word}")
        break

    hangmanWord = list(hangmanWord)
    print("Letters, that you entered:"+" ".join(playerLetters))
    playerLetter = input("Enter the letter: ").lower()
    if playerLetter in playerLetters:
        print("You entered that letter before!\n")
        continue
    else:
        playerLetters.append(playerLetter)
    print("")
    didPlayerGuessedTheLetter = False
    i = 0
    for x in word:
        if x == playerLetter:
            hangmanWord[i] = x
            didPlayerGuessedTheLetter = True
        i += 1
    if not didPlayerGuessedTheLetter:
        numberOfMistakes += 1
        if numberOfMistakes == 7:
            break
    print(draw_hangman(numberOfMistakes, word))

    hangmanWord = "".join(hangmanWord)

