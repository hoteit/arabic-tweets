# Server Setup for Tweet Collections

Using an Ubuntu 18.04.2 LTS instance,

- install `sudo apt-get install apache2 postgresql python3 virtualenv libapache2-mod-wsgi-py3`

- at `/etc/apache2/sites-available` create tweets.arabic.computer.conf and include the information below

```tweets.arabic.computer.conf Apache configuration
  <VirtualHost *:80>
    ServerName tweets.arabic.computer.conf
    ServerAdmin tarek@hoteit.net

    # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
    # error, crit, alert, emerg.
    LogLevel error
    ErrorLog ${APACHE_LOG_DIR}/tweets-search-error.log

    CustomLog ${APACHE_LOG_DIR}/tweets-access.log combined

    WSGIDaemonProcess arabic python-path=/var/www/arabic:/var/www/arabic/env/lib/python
  /site-packages
    WSGIProcessGroup arabic
    WSGIScriptAlias / /var/www/arabic/apache/wsgi.py process-group=arabic
    DirectoryIndex index.html index.php
    DocumentRoot /var/www/arabic/html
    <Directory /var/www/arabic/html>
            Require all granted
    </Directory>

    <Directory /var/www/arabic/apache>
            Require all granted
    </Directory>

    Alias /static/ /var/www/arabic/arabictweets/static/
    <Directory /var/www/arabic/arabictweets/static/>
            Require all granted
    </Directory>
</VirtualHost>
```

- In the home directory of the server clone the code from `git@github.com:hoteit/arabic.git`. Note make sure you have included the public ecryption key using `ssh-keygen` onto the github code ssh-deployment keys otherwise you will need to use `https://github.com/hoteit/arabic.git` with username and password to grab the data.

- create the virtual directory `sudo mkdir -p /var/www/arabic` then setup permissions `sudo chown tarek:tarek /var/www/arabic`

- copy the files from the local directory onto `/var/www/arabic`, such as `cp -R ~/arabic/* /var/www/arabic`

- setup a Python environment inside the server directory `virtualenv --python=python3 /var/www/arabic/env` then activate the virtual environment `source /var/www/arabic/env/bin/activate`

- install the Python code requirements while in the virtual environment (you would know that you are in the virtual environment if you see *env* listed in the terminal path) `(env) pip install -r /var/www/arabic/requirements.txt`

- because Python version may change, we need to create a symbolic link the current Python X.XX version in the virtual directory and call it just Python. `(env) ln -s /var/www/arabic/env/lib/python3.6 /var/www/arabic/env/lib/python`. That way if we had to change the Python version, we do not need to update Apache settings each and every time

- another annoying issue is that Djang admin image files would break unless we add a symbolic link of Django admin static files as part of /var/www/arabic/arabictweets/static. Run `(env) ln -s /var/www/arabic/env/lib/python/site-packages/django/contrib/admin/static/admin /var/www/arabic/arabictweets/static/admin`

- update the Django application settings to support the local database and local paths. In `/var/www/arabic/arabic/settings.py` under Databases, replace `'HOST': 'db'` with `'HOST': 'localhost'` and add `'PASSWORD': ''`

- to setup the password, first login into postgres using the command `sudo -i -u postgres` followed by `psql`. After that `ALTER USER Postgres WITH PASSWORD '<newpassword>';` followed by `\q`

- 