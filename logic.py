import requests
import json
import pprint as pp

KEY = 'AIzaSyCBtjf6MEDd1ZOVSOJ-M5WFcMT2U_8Y8Eg'
url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations="
url2 = "SL4 4AY"
url3 = "&origins="
url4 = "SL4 1QF"
url5 = "&units=imperial&key="
url_f = url1 + url2 + url3 + url4 + url5 + KEY

output = requests.get(url_f).json()
#pp.pprint(output)
a = output['rows'][0]['elements'][0]['distance']['value']
print(a)