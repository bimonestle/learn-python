def maxMinNumb():
    total = 0
    smallest = None
    largest = None

    print("Smallest before: ", smallest)
    print("Largest before: ", largest)
    
    numbers = input("Enter a list of numbers separated by space: ")
    listNumb = numbers.split()

    print(listNumb)

    maxNumber = maxNumb(listNumb)
    minNumber = minNumb(listNumb)
    print("Max number is: ", maxNumber, ", Min number is: ", minNumber)

def maxNumb(numbers):
    largest = None
    for number in numbers:
        number = int(number)
        if largest is None or number  > largest:
            largest = number
        print("Loop: ", number, largest)
    return largest

def minNumb(numbers):
    smallest = None
    for number in numbers:
        number = int(number)
        if smallest is None or int(number) < smallest:
            smallest = number
        print("Loop: ", number, smallest)
    return smallest

maxMinNumb()