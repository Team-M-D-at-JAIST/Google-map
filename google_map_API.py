# Google Cloud API key: AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y

import urllib.request, json
import urllib.parse
import requests


def directions_api(origin, destination,
                   mode = 'driving',
                   avoid = '',
                   departure_time = '',
                   arrival_time = '',
                   transit_routing_preference = ''):
    # Only 'origin' and 'destination' in arguments are necessary
    # Available mode parameter: driving walking bicycling transit
    # if set mode to transit, further details can be set such as "departure_time", "arrival_time", "transit_mode", etc.

    # Connect with Google Maps Platform (Directions API)
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y'

    origin = origin.replace(' ', '+')
    destination = destination.replace(' ', '+')

    # Make request from arguments
    nav_request = 'language=ja&origin={}&destination={}&mode={}&avoid={}&transit_routing_preference={}&key={}'\
        .format(origin,destination,mode,avoid,transit_routing_preference,api_key)
    nav_request = urllib.parse.quote_plus(nav_request, safe='=&')
    request = endpoint + nav_request

    # Run the Google Maps Platform Directions API
    response = urllib.request.urlopen(request).read()

    # Get the JSON response
    response = json.loads(response)

    return response

# #所要時間を取得
# for key in directions['routes']:
#     #print(key) # titleのみ参照
#     #print(key['legs'])
#     for key2 in key['legs']:
#         print('')
#         print('=====')
#         print(origin,"から",destination,"までの距離は",key2['distance']['text'],"です")
#         print("所要時間は",key2['duration']['text'],"です")
#         print('=====')
#
# print(directions)


def geocoding(place):
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
    api_key = 'AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y'
    address = 'address='+place

    url = endpoint+address+'&key='+api_key
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text
    response = json.loads(response)

    return response


def place_api(requested_api, place, query=''):
    # Available requested_api type:findplacefromtext, nearbysearch, textsearch, details...
    # Connect with Google Maps Platform (Directions API)

    endpoint = 'https://maps.googleapis.com/maps/api/place/'+requested_api+'/json?'
    api_key = 'AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y'

    # required parameters for "findplacefromtext"
    input = 'input='+ place
    # required parameters for "nearbysearch" and optimal parameters for "textsearch"
    location = ('location='+str(geocoding(place)['results'][0]['geometry']['location']['lat'])+','
                +str(geocoding(place)['results'][0]['geometry']['location']['lng']))
    print(location)
    # required parameters for "textsearch"
    query = 'query='+query
    print(query)

    if requested_api == 'findplacefromtext':
        url = endpoint+input+'&language=ja&inputtype=textquery&fields=formatted_address,name,rating,opening_hours,geometry&key='+api_key
    elif requested_api == 'nearbysearch':
        url = endpoint+location+'&language=ja&radius=1500&type=restaurant&keyword=cruise&key='+api_key
    elif requested_api == 'textsearch':
        url = endpoint+query+'&'+location+'&language=ja&key='+api_key

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text
    print(response)
    response = json.loads(response)

    return response


# place_api('findplacefromtext', '梅田駅')
# place_api('nearbysearch', '梅田駅')
# place_api('textsearch', '梅田駅', 'レストラン')
origin = "梅田駅"
destination = "京都駅"
directions_api(origin, destination)