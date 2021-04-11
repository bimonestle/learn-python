# Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max() and min() functions
# to compute the maximum and minimum numbers after the loop completes.

numbers = list()

while True:
    numb = input("Enter a number: ")

    if numb == "done":
        break
    try:
        numb = float(numb)
        numbers.append(numb)
    except:
        print("Invalid input")
        continue

print(numbers)
print("Maximum numbers:", max(numbers))
print("Minimum numbers:", min(numbers))