# -*- coding: utf-8 -*-
from io import BytesIO
from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError
from show_people.models import Document


class CommandPeopleOutputTests(TestCase):

    def setUp(self):
        call_command('loaddata', 'initial_data.json')

    def test_command_output_single_education(self):
        out = BytesIO()
        call_command('people', 'python', stdout=out)
        out = out.getvalue()
        python = Document.objects.filter(education='python')
        self.assertIn('People by education python', out)
        for i in python:
            self.assertIn('%s %s' % (i.person.first_name,
                                     i.person.last_name), out)

    def test_command_output_multi_education(self):
        out = BytesIO()
        call_command('people', 'python', 'java', stdout=out)
        out = out.getvalue()
        python = Document.objects.filter(education='python')
        self.assertIn('People by education python', out)
        for i in python:
            self.assertIn('%s %s' % (i.person.first_name,
                                     i.person.last_name), out)
        java = Document.objects.filter(education='java')
        self.assertIn('People by education java', out)
        for i in java:
            self.assertIn('%s %s' % (i.person.first_name,
                                     i.person.last_name), out)

    def test_command_output_invalid_education(self):
        out = BytesIO()
        self.assertRaisesMessage(CommandError,
                                 'People with "php" education does not exist',
                                 call_command, 'people', 'php', stdout=out)
