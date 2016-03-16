# -*- coding: utf-8 -*-
import os
import urllib
import json
from django.conf import settings


URL = 'http://api.openweathermap.org/data/2.5/weather?id=%s&appid=a60d882267c364f276f3dfea65e7d1f7'


def get_city_id(city):
    with open(os.path.join(settings.BASE_DIR, 'show_weather/city.list.json'), 'r') as file:
        for line in file:
            if city in line:
                return line.split(':')[1]


def get_weather(city):
    city_id = get_city_id(city)
    return json.loads(urllib.urlopen(URL % city_id).read())
