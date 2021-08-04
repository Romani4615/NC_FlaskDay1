from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from config import Config

app = Flask(__name__)
#instance of object allows to create web app, doing all the work-routes into real things
app.config.from_object(Config)
#Grab config class from config file, and add to config from app to use class
##app = instance of class^
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#OBJECT RELATIONAL MAPPER
from app import routes, models
#reads routes after creating the instance
#reads models from app(init we created)

