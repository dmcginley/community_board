# CommunityBoard

CommunityBoard is a Django-based web application designed to foster online discussions and interactions. It provides a content management system (CMS) for administrators, user profiles, and features for creating and managing categories, posts, and comments. More features will be added in future updates.

## Features

- **Admin CMS**: Manage users, categories, posts, and comments with an intuitive admin panel.
- **User Profiles**: Each user has a profile that can be customized.
- **Hero Section Editing**: Admins can update the hero section content dynamically.
- **Categories & Posts**: Users can create and browse categories and posts.
- **Comments System**: Engage in discussions with a commenting feature.
- **More Features Coming Soon**: Additional functionalities will be added in future updates.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/communityboard.git
   cd communityboard
   ```
2. **Create a Virtual Environment** (Recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Create a Superuser**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.
6. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`

## Configuration

- **Admin Panel**: Visit `/admin/` to manage the content.
- **Hero Section**: Editable via the admin CMS.
- **User Authentication**: Sign up, log in, and manage user profiles.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.



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




As root from /home/litedev-comunityboard/htdocs/comunityboard.litedev.dev start venv with:
```
source env/bin/activate

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

Once app is live you can create an admin user
```
python manage.py createsuperuser
```



## License

This project is licensed under the MIT License.

## Contact

For inquiries, reach out to **[Your Name]** at **hello@litedev.dev** or create an issue in the repository.

---
_Stay tuned for more updates!_



