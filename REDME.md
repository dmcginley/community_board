# Deploy Django Python App on CloudPanel

```
sudo apt update
```
To give the litedev user both read and write access 

```
ls -la
```
```
sudo chown -R litedev:litedev /home/litedev/htdocs/litedev.dev
```
```
sudo chmod -R u+rw /home/litedev/htdocs/litedev.dev
```

## Create a virtual environment:

```
python3 -m venv env
```

## Activate the virtual environment

```
source env/bin/activate
```
```
pip install -r requirements.txt
```
```
pip install django gunicorn psycopg2-binary
```
```
pip install mysqlclient
```

## Start project in current folder
```
django-admin startproject project .
```
## Change db to an sql db
### DATABASES example
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'litedev-db',
        'USER': 'litedev-db-user',
        'PASSWORD': 'R5RC66qHNCT5d1IR9DBq',
        'HOST': '127.0.0.1',  # Or specify the hostname of your MySQL server
        'PORT': '3306',       # MySQL default port
    }
}

```


## Migrate your database
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
## Let’s allow access to our port through the firewall.
```
ufw allow 8090
```
```
deactivate
```


## Gunicorn socket

Go to /etc/systemd/system in filezilla
nano /etc/systemd/system/gunicorn.socket

Copy/paste this code there then save the file:

	[Unit]
	Description=gunicorn socket

	[Socket]
	ListenStream=/run/gunicorn.sock

	[Install]
	WantedBy=sockets.target

	Enable the Gunicorn socket

	systemctl start gunicorn.socket
	systemctl enable gunicorn.socket


	systemctl start gunicorn-comunityboard.socket
	systemctl enable gunicorn-comunityboard.socket




To check the status of the Gunicorn socket, type the following command:
```
systemctl status gunicorn.socket
```
```
systemctl status gunicorn-comunityboard.socket
```

### Restarting gunicorn-comunityboard
```
sudo systemctl daemon-reload
```
```
sudo systemctl restart gunicorn-comunityboard
```
```
sudo systemctl status gunicorn-comunityboard
```

Creating an admin user
```
python manage.py createsuperuser
```




