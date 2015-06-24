from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template, session, jsonify
from modelsCode import *

#	respond to request form web server
#	each function maps to a request url


#http://localhost:5001/ || #http://localhost:5001/index
# 'href="{{ url_for('index') }}"'
@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
	return render_template('index.html', user = session)





# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'