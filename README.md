# django_app
## django document
https://docs.djangoproject.com/ja/4.2/

# activate venv
cd ~/django_app
source .venv/bin/activate

# install python library
pip install -r requirements.txt

# start app
python manage.py runserver

# create data_table
cd ./django_app/django/microblog python manage.py makemigrations
python manage.py migrate
