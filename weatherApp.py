#Powered By Dark Sky - https://darksky.net/poweredby/

import requests
import json
import time
import geocoding

def getPrettyCurrent(weatherData, geoData):
    if 'currently' in weatherData:
        currentWeather = weatherData['currently']
        result = u'===== {} =====\n{}\nOpis: {}\nTemperatura odczuwalna: {}\u2103\nZachmurzenie: {}%\nWilgotno\u015B\u0107: {}%\n'.format(
            geocoding.getFullName(geoData),
            getDataTimeCurrent(weatherData),
            currentWeather['summary'],
            currentWeather['apparentTemperature'],
            int(currentWeather['cloudCover']*100),
            int(currentWeather['humidity']*100),
        )
        if currentWeather['precipIntensity'] != 0:
            result += 'Opady atmosferyczne: {}mm\n'.format(currentWeather['precipIntensity'])
        else:
            result += u'Brak opad\u00F3w atmosferycznych.\n'
        return result

def getAllCurrent(data):
    result = ''
    if 'currently' in data:
        for property, data in data['currently'].items():
            result += u"{}: {}\n".format(property, data)
        return result
    else:
        return None

def getDataTimeCurrent(data):
    if 'currently' in data:
        return time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(data['currently']['time'] + data['offset']*3600))
    else:
        return None

def requestWeatherData(location):
    baseURL = 'https://api.darksky.net/forecast'
    secretKey = 'YOUR_KEY_HERE'
    parameters = {'lang':'pl', 'units':'si', 'exclude':'[flags,minutely]'}

    return requests.get('{}/{}/{}'.format(baseURL, secretKey, location), params = parameters)

if __name__ == '__main__':
    with open('weatherData.json', 'r') as f:
        #f.write(json.dumps(data, indent=4))
        data = json.load(f)
        print getAllCurrent(data)
'''
    address = geocoding.askForAddress()
    geoData = geocoding.requestGeoData(address)
    latLng = ','.join([str(i) for i in geocoding.getLatLng(geoData)])
    response = requestWeatherData(latLng)
    if response.status_code == 200:
        data = response.json()'''
    #print getDataTimeCurrent(data)
    #print getPrettyCurrent(data, geoData)
