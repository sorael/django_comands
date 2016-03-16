# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from show_weather.utils import get_weather


class Command(BaseCommand):

    help = 'Prints weather by city'

    def add_arguments(self, parser):
        parser.add_argument('city', type=str)

    def handle(self, *args, **options):
        city = options['city']
        weather = get_weather(city[0].upper() + city[1:].lower())
        try:
            self.stdout.write('Weather in %s city:' % weather['name'])
            self.stdout.write('Sky: %s' % weather['weather'][0]['description'])
            t = int(weather['main']['temp']) - 273.15
            self.stdout.write('Temperature: %s C' % t)
            self.stdout.write('Humidity: %s %%' % weather['main']['humidity'])
            self.stdout.write('Wind speed: %s m/s' % weather['wind']['speed'])
        except:
            raise CommandError('City "%s" does not find' % city)
