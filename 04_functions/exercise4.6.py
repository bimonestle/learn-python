hours = input("Enter hours:\n")
rate = input("Enter rate:\n")

def computepay(hours, rate):
    try:
        fHours = float(hours)
        fRate = float(rate)
        pay = fHours * fRate

        if fHours > 40.0:
            pay = 40.0 * fRate + (fRate * 1.5 * (fHours - 40.0))

        return pay
    except:
        return "Cannot calculate! Please enter numeric input"

print("Pay:", computepay(hours, rate))