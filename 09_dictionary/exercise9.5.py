# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from
# (i.e., the whole email address). At the end of the program,
# print out the contents of your dictionary.

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("There is no file: %s" % fName)
    quit()

domains = dict()
for line in fHand:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        address = words[1].split("@")
        domain = address[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)