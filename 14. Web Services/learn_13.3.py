# PARSING A JSON

import json

data = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "009",
        "x": "9",
        "name": "Brent"
    }
]
'''

# 'json.loads' parse the JSON. (Convert the string into a JSON object/format)
info = json.loads(data)
print("User counts: %d" % (len(info)) )

# The returned data in a parsed JSON is simply native Python structures
# Don't need to use JSON library to extract data for each user
for user in info:
    print("Name %s" %(user['name']))
    print("ID %s" %(user['id']))
    print("Attribute %s" %(user['x']))