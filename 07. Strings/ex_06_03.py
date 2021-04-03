# Encapsulate this code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.

def countLetter(word, letter):
    count = 0
    for alphabet in word:
        if alphabet == letter:
            count += 1
    print(count)

word = input("Enter word: ")
letter = input("Enter letter: ")
countLetter(word, letter)