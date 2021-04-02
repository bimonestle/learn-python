smallest = None
largest = None

print("Smallest before: ", smallest)
print("Largest before: ", largest)

numbers = input("Enter a list of numbers separated by space: ")
listNumb = numbers.split()

print(listNumb)

for number in listNumb:
    number = int(number)
    if largest is None or number > largest:
        largest = number
    print("Loop largest: ", number, largest)

    if smallest is None or number < smallest:
        smallest = number
    print("Loop smallest: ", number, smallest)

print("Max number is: ", largest, ", Min number is: ", smallest)