from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template
from models import *



@app.route('/welcome')
@app.route('/welcome/')
def welcome():
    user = Users.query.count()
    return render_template('welcome/page1.html', user = user)





