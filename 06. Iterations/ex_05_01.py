def calcNumb():
    count = 0
    total = 0.0
    while True:
        number = input("Enter a number: ")
        if number == "done":
            break
        try:
            number = float(number)
            total += number
            count += 1
        except:
            print("Invalid input")
    print("Total: ", total, "Count: ", count, "Average: ", total/count)

calcNumb()