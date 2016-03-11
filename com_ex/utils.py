# -*- coding: utf-8 -*-
import urllib
import json


URL = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=a60d882267c364f276f3dfea65e7d1f7'


def get_weather(city):
    return json.loads(urllib.urlopen(URL % city).read())
