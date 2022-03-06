smallest = None
largest = None
while True:
    numb = input('Enter a number: ')
    if numb == 'done':
        break
    try:
        fNumb = float(numb)
        if smallest is None or fNumb < smallest:
            smallest = fNumb
        if largest is None or fNumb > largest:
            largest = fNumb
    except:
        print("Invalid input!")

print("Min:", smallest,"\n","Max:", largest)