from datetime import timedelta

# General
DEBUG = True
SECRET_KEY = 'B\xee\xaa\xceb~\x95\xb9\xe5\x0f\x80\x8f\n\xad\xa1\xc8\xaa\x90nntj\xb3\xbf'

# DB
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zermatt:zemn55P!at@localhost/zermatt'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT
JWT_TOKEN_LOCATION = 'cookies'
JWT_COOKIE_CSRF_PROTECT = False
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
JWT_COOKIE_SECURE = True

# Mail
MAIL_HOST = 'asmtp.mail.hostpoint.ch'
MAIL_PORT = '465'
MAIL_LOGIN_USER = 'kly7@247.ch'
MAIL_LOGIN_PASS = 'brasil'
MAIL_FROM = 'Zermatt Reservation <pat@247.ch>'
