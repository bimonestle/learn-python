# This program records the domain name (instead of the address)
# where the message was sent from instead of
# who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fName = input("Enter file name: ")

try:
    fHand = open(fName)
except:
    print("File cannot be opened:", fName)
    exit()

domain = dict()
for line in fHand:
    line = line.rstrip()

    if line.startswith("From "):
        # test print line
        # print(line)
        words = line.split()

        # Email address
        sender = words[1]

        # get the position of the domain name
        domStart = sender.find("@") + 1

        # get domain name by slicing the email address
        domainName = sender[domStart:]

        # Get the domain name from the particular line and count it.
        # The longer version to get the result.
        # if domainName not in domain:
        #     domain[domainName] = 1
        # else:
        #     domain[domainName] += 1

        # The more succinct alternative
        domain[domainName] = domain.get(domainName, 0) + 1
print(domain)