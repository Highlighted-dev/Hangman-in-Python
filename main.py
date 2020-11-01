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

while True:
    if "_" in list(hangmanWord):
        print(hangmanWord)
    else:
        print(f"Congratulations, you won! The word was {word}")
        break
    didPlayerGuessedTheLetter = False
    i = 0
    hangmanWord = list(hangmanWord)
    print("Letters, that you entered:"+" ".join(playerLetters))
    playerLetter = input("Enter the letter: ").lower()
    if playerLetter in playerLetters:
        print("You entered that letter before!\n")
        continue
    else:
        playerLetters.append(playerLetter)
    print("")
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

