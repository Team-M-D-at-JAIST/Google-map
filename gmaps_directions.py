# Google Cloud API: AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y

import urllib.request, json
import urllib.parse

#Google Maps Platform Directions API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyDoXPAkFCL2EehpIX0FW8_IEZSEUGap7_Y'

#出発地、目的地を入力
origin = input('出発地を入力: ').replace(' ','+')
destination = input('目的地を入力: ').replace(' ','+')

#avalible mode parameter: driving walking bicycling transit
#if set mode to transit, further details can be set such as "departure_time", "arrival_time", "transit_mode", etc.
mode = input('交通手段を入力: ').replace(' ','+')
print(mode)

avoid = ''
departure_time = ''
arrival_time = ''
transit_routing_preference = ''



#パラメータです、originと&destinationだけが必要
nav_request = 'language=ja&origin={}&destination={}&mode={}&avoid={}&transit_routing_preference={}&key={}'\
    .format(origin,destination,mode,avoid,transit_routing_preference,api_key)
nav_request = urllib.parse.quote_plus(nav_request, safe='=&')
request = endpoint + nav_request

print('')
print('=====')
print('url')
print(request)
print('=====')

#Google Maps Platform Directions APIを実行
response = urllib.request.urlopen(request).read()

#結果(JSON)を取得
directions = json.loads(response)

#所要時間を取得
for key in directions['routes']:
    #print(key) # titleのみ参照
    #print(key['legs'])
    for key2 in key['legs']:
        print('')
        print('=====')
        print(origin,"から",destination,"までの距離は",key2['distance']['text'],"です")
        print("所要時間は",key2['duration']['text'],"です")
        print('=====')

print(directions)
