inp = input("Enter fahrenheit temperature:\n")
try:
    fahr = float(inp)
    cels = (fahr - 32) / (9/5)
    print(cels, "F")
except:
    print("This is not a number")