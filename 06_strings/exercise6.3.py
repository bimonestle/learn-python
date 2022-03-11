def count(letter: str, word: str) -> int:
    count = 0
    for l in word:
        if l == letter:
            count += 1
    
    print("The letter", letter, "is counted", count, "times")

word = input('Enter word: ')
letter = input('Enter searched letter: ')
count(letter, word)