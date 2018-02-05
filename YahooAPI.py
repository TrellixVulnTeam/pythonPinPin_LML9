import urllib.parse
import urllib.request
import requests
import json
import xml.etree.ElementTree as et
import xml.dom.minidom as mi
from bs4 import BeautifulSoup


def yahooapi(choice):
    # montreal 3534
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid in(select woeid from geo.places(1) where text='montreal,qc') and u='c'"
    if choice=='json':
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + '&format=json'
        print (yql_url)
        result = urllib.request.urlopen(yql_url)
        r=result.read()
        print (result.getcode(),result.info)
        data = json.loads(r)
        pp_json(data)
        print('temprature(c)=', data['query']['results']['channel']['item']['condition']['temp'])
        print (data['query']['results'])
    elif choice=='xml':
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query})
        result = urllib.request.urlopen(yql_url)
        r=result.read()
        pp_xml(r)
        print(result.getcode())


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def pp_xml(xmlString):
    # tree=et.ElementTree(str(xmlString,'utf-8'))
    # tree=et.fromstring(xmlString)
    # root=tree.getroot()
    xml=mi.parseString(xmlString)
    pretty_xml_as_string=xml.toprettyxml()
    print(pretty_xml_as_string)
    for e in xml.getElementsByTagName('yweather:forecast'):
        print('weather forcast:',e.getAttribute("date"),e.getAttribute('text'),'temp.high:',e.getAttribute('high'),'temp low:',e.getAttribute('low') )


# yahooapi('json')
yahooapi('xml')