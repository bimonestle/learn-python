score = input("Enter score: ")

def computeGrade(score):
    try:
        fScore = float(score)
        if fScore >= 0.9 and fScore <= 1.0:
            return "A"
        elif fScore >= 0.8 and fScore < 0.9:
            return "B"
        elif fScore >= 0.7 and fScore < 0.8:
            return "C"
        elif fScore >= 0.6 and fScore < 0.7:
            return "D"
        else:
            return "F"

    except:
        return "Bad score"

print(computeGrade(score))