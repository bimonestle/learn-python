import re

s = "A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM"
lst = re.findall("\S+@\S+", s)
print(lst)

# The findall() method searches the string in the second argument
# and returns a list of strings which look like an email address
# We are using a two-character sequence that matches a non-whitespace character '\S'