# Install
    apt install python-virtualenv libmysqlclient-dev
    pyvenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata testdata

* You will also need a LastFM account and a API account from http://www.last.fm/api/account
* Create a local\_settings.py and set your own LASTFM\_APIKEY and LASTFM\_API\_SECRET

# Usage
- Create an admin user: python manage.py createsuperuser
- Goto /admin, login, then add a LastFMUser and make it active.
- Setup your music player (f.ex Spotify) to scrobble to that LastFM account.
- Goto / and you should be set :=)
