# Overview
Just example of simple django management commands

# Requirements
* Python (2.7)
* Django (1.8)

# To install project follow instruction
Enter this in your favorite console:
1) git clone git@github.com:sorael/django_commands.git
2) cd django_commands
3) pip install -r requirements.txt
4) ./ manage.py syncdb
5) ./ manage.py loaddata initial_data.json

# Usage commands:
* people (you can enter multiple educations separated by a space)
./ manage.py people {education}

* weather (you can enter only one city)
./ manage.py weather {city}