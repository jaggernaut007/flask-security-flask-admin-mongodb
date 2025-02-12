from datetime import timedelta
import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#    python -c "import os; print(repr(os.urandom(24)));"
SECRET_KEY = 'DO_NOT_use_Unsecure_Secrets_in_production_environments'
COOKIE_SECURE = 'Secure'
COOKIE_DURATION = timedelta(days=365)

# MongoDB Config
MONGODB_DB = 'mydatabase'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# Flask Security
SECURITY_PASSWORD_SALT = 'DO_NOT_use_Unsecure_Secrets_in_production'
SECURITY_REGISTERABLE = True
SECURITY_POST_LOGIN_VIEW = 'members.member_page'
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True


# i18n
BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'translations/')

BABEL_DEFAULT_LOCALE = 'en_US'

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps"
# to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps
# (near the bottom).


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'yourname@gmail.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Your Name" <yourname@gmail.com>'

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
]
