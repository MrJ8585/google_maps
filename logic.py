import requests
import json
import pprint as pp

a = [31.870639771466692, -116.60239684850126]
b = [31.866112295013266, -116.58939107764003]
KEY = 'AIzaSyCBtjf6MEDd1ZOVSOJ-M5WFcMT2U_8Y8Eg'
url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations="
url2 = str(a[0]) + ',' + str(a[1])
url3 = "&origins="
url4 = str(b[0]) + ',' +  str(b[1])
url5 = "&units=imperial&key="
url_f = url1 + url2 + url3 + url4 + url5 + KEY
print(url_f)
output = requests.get(url_f).json()
a = output['rows'][0]['elements'][0]['distance']['value']
print(a)