# -*- coding: utf-8 -*-
import urllib
import json


URL = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=44db6a862fba0b067b1930da0d769e98'


def get_weather(city):
    return json.loads(urllib.urlopen(URL % city).read())
