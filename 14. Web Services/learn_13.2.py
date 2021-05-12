# LOOPING THROUGH NODES

# The following program, loop through all of the 'user' nodes.

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)

# The findall method retrieves a list of subtrees which represents
# the 'user' structures in the XML tree.
lst = stuff.findall('users/user')
print('User count:', len(lst))

# Look at each of the user nodes.
# Prints the 'name', 'id' text elements
# as well as the 'x' attribute from the 'user' node.
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))



# It's important to include all the
# parent level elements in the 'findall' statement except ('users/user')
# except for the top level element.
# Otherwise, Python will not find any desired nodes.

# 'lst' stores all 'user' elements that are nested
# within their 'user' parent.
lst = stuff.findall('users/user')
print("User count: %d" % (len(lst)))

# 'lst2' looks for user elements that are not nested within
# the top level 'stuff' element where there are none
lst2 = stuff.findall('user')
print("User count: %d" % (len(lst2)))