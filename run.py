from flask import Flask
import os
app = Flask(__name__)

class Config:
    """
        setup config vars 4 flask
        ENVIRONMNENTAL VARIABLES
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

##app = instance of class^
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#@app.route('/test')
#def test():
#    return 'This a test'
# MUST ADD /test TO SEE THE ROUTE