# Music project install instructions

```shell
    git clone git@github.com:tutorials-4newbies/music_project.git
    cd music_project
```


Create a python virtual enviorment and install all requirements
```shell
python -m venv NAME_OF_VENV
```

Windows:
```shell
NAME_OF_VENV\Scripts\activate.bat
```

Linux \ Mac
```shell
source NAME_OF_VENV\bin\activate
```

```shell
(NAME_OF_VENV) pip install -r requirements.txt
```

create the database structure
```shell
python manage.py migrate
```

add a super user to work with
```shell
python manage.py createsuperuser
```


Run server
```shell
python manage.py runserver
```

If you know how connect project to IDE



