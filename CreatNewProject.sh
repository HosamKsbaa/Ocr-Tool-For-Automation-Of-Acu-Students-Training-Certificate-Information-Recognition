pip install virtualenv
virtualenv -p python3 env
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
MyFirstProject/env/scripts/activate
pip install django
django-admin 
django-admin startproject MyFirstProject 
cd MyFirstProject


python manage.py runserver
python manage.py startapp base


python  manage.py migrate 
python  manage.py run server

# apply  migrations
python  manage.py makemigrations
python  manage.py migrate

#
MyFirstProject/env/scripts/activate
cd MyFirstProject
python manage.py runserver 127.0.0.1:8001

#Hosam 55555

python  manage.py createsuperuser

#


virtualenv -p python3 env
MyFirstProject/env/scripts/activate
