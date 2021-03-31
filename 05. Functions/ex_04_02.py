def computeGrade(score):
    if score >= 0.9 and score <= 1:
        print("A")
    elif score < 0.9 and score >= 0.8:
        print("B")
    elif score < 0.8 and score >= 0.7:
        print("C")
    elif score < 0.7 and score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Bad Score")

try:
    score = input("Enter score: ")
    score = float(score)
except:
    print("Bad score")
else:
    computeGrade(score)