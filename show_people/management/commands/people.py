# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from show_people.models import Person


class Command(BaseCommand):

    help = 'Prints all people by education'

    def add_arguments(self, parser):
        parser.add_argument('education', nargs='+', type=str)

    def handle(self, *args, **options):
        for education in options['education']:
            documents = Person.filter_by_education(education)
            if documents:
                self.stdout.write('People by education %s' % education)
                for document in documents:
                    self.stdout.write('%s %s' % (document.person.first_name,
                                                 document.person.last_name))
            else:
                raise CommandError('People with "%s" education does not exist'
                                   % education)
