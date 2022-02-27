# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program

hours = input("Enter hours:\n")
rate = input("Enter rate:\n")

try:
    fHours = float(hours)
    fRate = float(rate)

    pay = fRate * fHours

    if fHours > 40.0:
        pay = fRate * 40.0 + (fRate * 1.5 * (fHours - 40.0))
    
    print("Pay:", pay)

except:
    print("Please enter numeric input!")