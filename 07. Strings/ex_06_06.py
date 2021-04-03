# Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand how they work.

word = "banana"
print(word.capitalize())

word = "ßanana"
print(word.lower())
print(word.casefold())

word = "banana"
print(word.center(10, "s"))

word = "banana"
print(word.count("a"))

word = "banana"
print(word.encode("ascii"))

word = "banana"
print(word.endswith("a"))
print(word.endswith("A"))

word = "banana\tapple\tmelon"
print(word.expandtabs()) # default will have 8
print(word.expandtabs(14))

word = "bananas"
print(word.find("n"))
print(word.find("s"))
print(word.find("s",3))
print(word.find("s",4, 6))
print(word.find("x"))
print("s" in word)
print("sa" in word)

# ????????
word = "The sum of 1 + 2 is {0}"
print(word.format(1+2))

# ????????
word = "The sum of 1 + 2 is {0}"
# print(word.format_map())

word = "banana"
print(word.index("n"))
# print(word.index("x"))