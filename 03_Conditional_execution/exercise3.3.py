# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("Enter score:\n")
try:
    fScore = float(score)

    if fScore >= 0.9 and fScore <= 1.0:
        print("A")
    elif fScore >= 0.8 and fScore < 0.9:
        print("B")
    elif fScore >= 0.7 and fScore < 0.8:
        print("C")
    elif fScore >= 0.6 and fScore < 0.7:
        print("D")
    elif fScore < 0.6:
        print("F")
    else:
        print("Bad score")
except:
    print("Bad score")
