try:
    hours = float(input("Enter Hours: "))
except:
    print("Error. Please enter numeric input")
try:
    rate = float(input("Enter rate: "))
except:
    print("Error. Please enter numeric input")
else:
    pay = hours * rate
    if hours > 40 :
        basicPay = 40 * rate
        gap = hours - 40
        pay = (gap) * rate * 1.5 + basicPay
        print(pay)
    else :
        print(pay)