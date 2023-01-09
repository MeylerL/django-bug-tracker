# Django Bug Tracker

A work-in-progress first attempt at a django web app. You can access the live version [here](http://meylerl.pythonanywhere.com/)

## Installation
---
```
# Clone the repository
$ git clone https://github.com/Meylerl/django-bug-tracker

# Navigate to directory
$ cd .\django-bug-tracker  

# Create a virtual environment and activate it 
$ virtualenv env
$ .\env\Scripts\activate

# Install requirements 
$ pip install -r requirements.txt

# Navigate to app
$ cd BugTracker

# Create migrations and migrate into database
$ python manage.py makemigrations
$ python manage.py migrate

# Create a superuser 
$ python manage.py createsuperuser

# Start development server (localhost:8000)
$ python manage.py runserver
```
