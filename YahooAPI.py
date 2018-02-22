import urllib.parse
import urllib.request
from datetime import datetime

import pymysql
import requests
import json
import xml.etree.ElementTree as et
import xml.dom.minidom as mi
from bs4 import BeautifulSoup


def yahooapi(choice):
    # montreal 3534
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select * from weather.forecast where woeid in(select woeid from geo.places(1) where text='montreal,qc') and u='c'"
    if choice == 'json':
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + '&format=json'
        print(yql_url)
        result = urllib.request.urlopen(yql_url)
        r = result.read()
        print(result.getcode(), result.info)
        data = json.loads(r)
        pp_json(data)
        print('temprature(c)=', data['query']['results']['channel']['item']['condition']['temp'])
        forecastlist = data['query']['results']['channel']['item']['forecast']
        print('forecast=', forecastlist)
        forecast(forecastlist)
        # print (data['query']['results'])
    elif choice == 'xml':
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query})
        result = urllib.request.urlopen(yql_url)
        r = result.read()
        pp_xml(r)
        print(result.getcode())


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def forecast(forecastlist):
    db = pymysql.connect(host="127.0.0.1", port=3306, user="hbyzy", passwd="123456", db="yahooforecast")
    cursor = db.cursor()
    for e in forecastlist:
        code = int(e.get('code', 'wrong'))
        date = (datetime.strptime(e.get('date', 'wrong'), '%d %b %Y'))
        date = datetime.date(date)
        day = e.get('day', 'wrong')
        high = e.get('high', 'wrong')
        low = e.get('low', 'wrong')
        text = e.get('text', 'wrong')
        print(code, type(code), date, type(date), day, type(day), high, type(high), low, type(low), text, type(text))
        query =cursor.execute("insert into weather(code,date,day,high,low,text) values(%d,'%s','%s','%s','%s','%s')" % (code, date, day, high, low, text))
    db.commit()
    query= cursor.execute("select* from weather")
    queryresult=cursor.fetchall()
    for ele in queryresult:
        print("date:",ele[1]," ",ele[2]," weather like ",ele[5]," temp between ",ele[4]," to ",ele[3]," yahoo code is ",ele[0])
    cursor.close()
    db.close()


def pp_xml(xmlString):
    # tree=et.ElementTree(str(xmlString,'utf-8'))
    # tree=et.fromstring(xmlString)
    # root=tree.getroot()
    xml = mi.parseString(xmlString)
    pretty_xml_as_string = xml.toprettyxml()
    print(pretty_xml_as_string)
    for e in xml.getElementsByTagName('yweather:forecast'):
        print('weather forcast:', e.getAttribute("date"), e.getAttribute('text'), 'temp.high:', e.getAttribute('high'),
              'temp low:', e.getAttribute('low'))


# yahooapi('json')
yahooapi('json')
