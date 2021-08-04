import os

basedir = os.path.abspath(os.path.dirname(__file__))
# where project's saved
class Config:
   
        #setup config vars 4 flask
        #ENVIRONMNENTAL VARIABLES
    SECRET_KEY = 'a72491'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
