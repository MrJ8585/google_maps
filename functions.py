import random
import requests
import json
import pprint as pp

def node(x1, x2, y1, y2):
    si = x2 - x1
    no = abs(y2 - y1)
    aa = random.uniform(0, si)
    bb = random.uniform(0, no)
    a = x1 + aa
    b = y2 + bb
    if in_bounds(x1, x2, y1, y2, a, b):
        print([a,b])
        return [a,b]
    else:
        node(x1, x2, y1, y2)

def in_bounds(x1, x2, y1, y2, inputx, inputy):
    if (x1 <= inputx <= x2) and (y2 <= inputy <= y1):
        return True
    return False

def distance(a, b):

    KEY = 'AIzaSyCBtjf6MEDd1ZOVSOJ-M5WFcMT2U_8Y8Eg'
    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations="
    url2 = str(a[0]) + ',' + str(a[1])
    url3 = "&origins="
    url4 = str(b[0]) + ',' +  str(b[1])
    url5 = "&units=imperial&key="
    url_f = url1 + url2 + url3 + url4 + url5 + KEY

    output = requests.get(url_f).json()
    value = output['rows'][0]['elements'][0]['distance']['value']
    return value

def matrix(nodes):
    out = []
    for i in range(len(nodes)):
        curr = []
        for j in range(len(nodes)):
            if i == j:
                curr.append(-1)
            else:
                val = distance(nodes[i], nodes[j])
                curr.append(val)
        out.append(curr)
    return out