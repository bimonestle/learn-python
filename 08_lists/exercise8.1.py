# Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and
# returns a new list that contains all but the first and last elements.


def chop(l: list) -> None:
    l.pop(0)
    l.pop()
    return None

def middle(l: list) -> list:
    chop(l)
    print('middle:',l)
    return l

# t = ['pining', 'for', 'the', 'fjords']
# t = [3, 41, 12, 9, 74, 15]
newlist = list()
while True:
    inp = input('Enter new element: ')
    if inp == 'done':
        break
    if inp.isalpha():
        newlist.append(inp)
    else:
        numb = int(inp)
        newlist.append(inp)
middle(newlist)