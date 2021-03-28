hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate
if hours > 40 :
    basicPay = 40 * rate
    gap = hours - 40
    pay = (gap) * rate * 1.5 + basicPay
    print(pay)
else :
    print(pay)
