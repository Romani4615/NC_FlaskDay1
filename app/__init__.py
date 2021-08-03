from flask import Flask
from config import Config

app = Flask(__name__)
#instance of object allows to create web app, doing all the work-routes into real things
app.config.from_object(Config)
#Grab config class from config file, and add to config from app to use class

##app = instance of class^
from app import routes
#reads routes after creating the instance

