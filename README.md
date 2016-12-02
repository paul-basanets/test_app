### Training Django app
For educational purposes.

#### Installation

Clone Git repo
Create virtual env
```bash
/<your_venv>/bin/pip install -r requirements.txt
```

#### Running

**Dev server:**
```bash
/<your_venv>/bin/python manage.py runserver
```

**Production server:**

Do collectstatic at first:
 ```bash
/<your_venv>/bin/python manage.py collectstatic
```

Use WSGI app 'application' from wsgi.py

F.x. for uWSGI:
```
chdir = /opt/www/%(project)
module = wsgi:application
```

