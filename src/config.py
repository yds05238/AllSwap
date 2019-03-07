'''
  config.py 
  Backend Development Team

  Code that stores configurations for the AllSwap Web Application. 

THREADS_PER_PAGE = 2

DEBUG = True
SECRET_KEY = 'secret'

# flask-security
# --------------
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '$2a$10$WyxRXkzAICMHgmqhMGTlJu'
SECURITY_CONFIRMABLE = False
SECURITY_REGISTERABLE = True

# flask-sqlalchemy
# ----------------
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False 
SQLALCHEMY_ECHO = True 

SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

CLIENT_HOST = '0.0.0.0'
PORT = 5000


'''





