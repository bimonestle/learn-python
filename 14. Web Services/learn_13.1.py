# PARSING XML

import xml.etree.ElementTree as ET

# The triple single quotes can span multiple lines
data ='''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
'''

# 'formstring' Parse XML Document from string constant
tree = ET.fromstring(data)

# 'find' searches through the XML tree and
# retrieves the element that matches the specified tag
print("Name: %s" % (tree.find('name')).text)
print("Attr: %s" % (tree.find('email')).get("hide"))