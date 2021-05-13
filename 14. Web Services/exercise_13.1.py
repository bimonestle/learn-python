# Change either geojson.py or geoxml.py to print out the two-character country code
# from the retrieved data. Add error checking so your program does not traceback
# if the country code is not there. Once you have it working, search for “Atlantic Ocean”
# and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
api_key = input("Your API Key: ")

if api_key is False:
    api_key = 42
    serviceUrl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# ignore SSL certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceUrl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved %d characters' % (len(data)))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lat']
    
    print('lat: %s, lng: %s' % (lat, lng))


    location = js['results'][0]['formatted_address']
    addrComp = js['results'][0]['address_components']
    isCountry =  False
    try:
        for elem in addrComp:
            types = elem['types']
            if types == ['country', 'political']:
                isCountry = True
                print(location, ". The country code is '%s'" % (elem['short_name']))
        if not isCountry:
            raise Exception
    except:
        print("There is no country code for this location")