# Django
Start new project
-----------------
```
$ django-admin startproject [project name]
```

Run server
-----------
```
$ python manage.py runserver [IP:port]
```

Create an app
---------
```
$ python manage.py startapp [app name]
```

Setup database
---------
```
$ python manage.py migrate
```


Install our app config to project
-----
First open `[Project name]/setting.py`  
then look at `INSTALLED_APPS` and add
`'[app name].apps.[Config function name]'`  
Finally (Always use this when you've change database schema)  
```
$ python manage.py makemigrations [app name]
```

This command will change the python to SQL statements automatically(use this once).
```
$ python manage.py sqlmigrate polls 0001
```

After that we'll use these SQL statements to Database  
```
$ python manage.py migrate
```

Create an admin user
-----
```
$ python manage.py createsuperuser
```

Run TestCase
-----
```
$ python manage.py test [app name]
```
