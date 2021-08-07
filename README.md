# BamBank-App

Django Web Application for Bambank

## Instructions
* cd to desired locations
* git clone https://github.com/Alex-Sainsbury/BamBank-App.git
* cd Bambank-app
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt
* cd bambank_app
* python manage.py migrate
* python manage.py runserver
* open http://localhost:8000/


## TODO

* Prevent sending more Bambeuros than user has available
* Prevent user sending Bambeuros to themself
* Override Transaction form, change User Dropdown to be field where username can be entered