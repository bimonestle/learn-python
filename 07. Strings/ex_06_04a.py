# Parsing strings
# Get the hostname only

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

atpos = data.find("@")
print("@ position is at:", atpos)

sppos = data.find(" ", atpos)
print("The end of the host position is at:", sppos)

host = data[atpos+1:sppos]
print("The host name is:", host)