# Overview
Just example of simple django management commands

# Requirements
* Python (2.7)
* Django (1.8)

# To install project follow instruction
Enter this in your favorite console:

    git clone git@github.com:sorael/django_commands.git
    cd django_commands
    pip install -r requirements.txt
    ./ manage.py syncdb
    ./ manage.py loaddata initial_data.json

 

# Usage commands:
* people (you can enter multiple educations separated by a space)
    ./ manage.py people {education}
* weather (you can enter only one city)
    ./ manage.py weather {city}