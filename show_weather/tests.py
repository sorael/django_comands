# -*- coding: utf-8 -*-
from io import BytesIO
from django.test import TestCase
from django.core.management import call_command



class CommandWeatherOutputTests(TestCase):

    def test_command_output_single_city(self):
        out = BytesIO()
        call_command('weather', 'Kiev', stdout=out)
        out = out.getvalue()
        self.assertIn('Weather in', out)
        self.assertIn('Sky', out)
        self.assertIn('Temperature', out)
        self.assertIn('Humidity', out)
        self.assertIn('Wind speed', out)
