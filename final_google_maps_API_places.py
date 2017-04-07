import googlemaps
import json
import urllib

API_KEY = My_API_KEY

# todo: create def to call place details api based on the place id.
# todo: try to replace googlemaps library with the urlopen and json libraries


place_id_list = []


def get_place_details(location, radius, types, key):
    auth_key = key
    location = location
    radius = radius
    types = types  # list of types: https://developers.google.com/places/web-service/supported_types

    MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
             '?query={0}'
             '&radius={1}'
             '&types={2}'
             '&sensor=false&key={3}').format(location, radius, types, auth_key)
    return(MyURL)

    response = urllib.request.urlopen(MyUrl).read().decode('utf8')
    json_result = json.loads(response)

    for place in range(len(json_result['results'])):
        place_id = json_result['results'][place]['place_id']
        place_id_list.append(place_id)

get_place_details('liquor+store+in+NYC', 1000, 'liquor_store', API_KEY)

result_data = []
for _id in place_id_list:
    url = ('https://maps.googleapis.com/maps/api/place/details/json'
           '?placeid={0}&key={1}').format(_id, API_KEY)
    pl_response = urllib.request.urlopen(url).read().decode('utf8')
    pl_json_result = json.loads(pl_response)
    pl_name = pl_json_result['result']['name']
    try:
        pl_url = pl_json_result['result']['website']
    except:
        pl_url = 'NA'
    pl_address = pl_json_result['result']['formatted_address']
    pl_phone = pl_json_result['result']['formatted_phone_number']
    try:
        pl_open = pl_json_result['result']['opening_hours']['weekday_text']
    except:
        pl_open = 'NA'
    try:
        pl_review = pl_json_result['result']['rating']
    except:
        pl_review = 'NA'

    result_data.append({'name': pl_name,
                        'url': pl_url,
                        'address': pl_address,
                        'phone': pl_phone,
                        'hours': pl_open,
                        'rating': pl_review})
print(json.dumps(result_data,sort_keys= True, indent = 4))



# print(json.dumps(query_result, sort_keys=True, indent=4))  # print pretty

