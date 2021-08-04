from app import app, db
from flask import render_template
from app.forms import RegisterForm
from app.models import User


@app.route('/')
#takes a string/url rule
def index():
    name = 'Aaron'
    title = 'coding temple intro 2 flazk'
    return render_template('index.html', my_name=name, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('THE FORM IS VALID!')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username)
        # Create new instance of User
        new_user = User(username, email, password)
        
        # Add new user to db
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', title='Register for CT Squad Blog', form=form)
# MUST ADD/test TO SEE THE ROUTE