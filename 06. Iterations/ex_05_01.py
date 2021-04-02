def calcNumb():
    count = 0
    total = 0.0
    while True:
        number = input("Enter a number: ")
        if number == "done":
            break
        number = float(number)
        total += number
        count += 1
    print("Total: ", total, "Count: ", count, "Average: ", total/count)
try:
    calcNumb()
except:
    print("Invalid input")