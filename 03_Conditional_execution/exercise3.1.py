# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = input("Enter hours:\n")
fHours = float(hours)
rate = input("Enter rate:\n")
fRate = float(rate)
pay = fHours * fRate

if fHours > 40.0:
    pay = fRate * 40.0 + (fRate * 1.5 * (fHours-40.0))

print("Pay:", pay)