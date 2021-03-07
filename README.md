# Project bppd
You can visit this project website on https://triefauzan-bppd-project.herokuapp.com/

# Setup

Download/clone this repository and switch to the directory

```
$ cd path/to/this/project
```

Create virtual environtment and activate the virtualenv

```
$ python -m venv .env

$ source .env/bin/activate
```

Install project dependencies:

```
$ pip install -r requirements.txt
```

Visit https://djecrety.ir/ to generate secret key and add to settings.py
```
...
SECRET_KEY = your_secret-key
...
```
Set your database in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply the migrations:
```
$ python manage.py migrate
```
You can now run the development server:
```
$ python manage.py runserver
```
