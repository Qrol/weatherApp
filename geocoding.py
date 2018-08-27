import requests
import json

askForAddress = lambda: raw_input("Input address: ")

def createURL(address):
    baseURL = 'http://www.datasciencetoolkit.org/maps/api/geocode/json?address='
    address = '+'.join(address.split())
    return baseURL + address

def requestGeoData(address):
    response = requests.get(createURL(address))
    if response.status_code == 200:
        results = response.json()['results']
        if len(results) == 1:
            return results[0]
        else:
            return None
    else:
        print "Error {}: {}".format(response.status_code, response.reason)
        return None

def getLatLng(data):
    latAndLng = data['geometry']['location']
    return latAndLng['lat'], latAndLng['lng']

def getFullName(data):
    nameParts = [comp['short_name'] for comp in data['address_components']]
    result = ', '.join(nameParts)
    return result#json.dumps(data, indent=4)

if __name__ == '__main__':
    address = askForAddress()
    data = requestGeoData(address)
    if data:
        print getFullName(data)
        print getLatLng(data)
