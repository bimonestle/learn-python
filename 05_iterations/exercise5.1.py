count = 0
total = 0
while True:
    numb = input('Enter a number: ')
    if numb == 'done':
            break
    try:
        fNumb = float(numb)
        count += 1
        total += fNumb
    except:
        print("Invalid input")
print(total, count, total/count)