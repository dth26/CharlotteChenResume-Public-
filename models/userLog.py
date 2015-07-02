from app import app
from flask import render_template, request, session, redirect, url_for
from models import *
from passlib.apps import custom_app_context as pwd_context


basedir = "/home/pythonprogrammer/mysite/"


# user verification on login
# assign admin privileges
# if user not found in table, user will not recieve privileges
@app.route('/login', methods=['GET', 'POST'])
def login():
	name = request.form.get('name')
	password = request.form.get('password')

	#if request.method == 'POST':
	user = Users.query.filter_by(firstName=name)

	if user.count() > 0 and pwd_context.verify(password, user[0].hashedPassword):
	    session['username'] = user[0].firstName
	    session['lastName'] = user[0].lastName
	    session['privileges'] = user[0].privileges
	    session['city'] = user[0].city
	    session['state'] = user[0].state
	    session['phone'] = user[0].phone
	    return render_template('index.html', user = session)
	else:
	    session.pop('username', None)
	    return render_template('loginError.html', user = session)



# logout and remove user privileges
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/createUser',methods=['POST'])
def createUser():
    username = request.form.get('username')
    lastname = request.form.get('lastname')
    password = request.form.get('password')
    state = request.form.get('state')
    city = request.form.get('city')
    phone = request.form.get('phone')
    email = request.form.get('email')

    createNewUser(username,lastname, password,state,city,phone,email)

    return redirect(url_for('index'))



# set the secret key.  keep this really secret:
# create a session
# any script that uses session must add this line of code
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


















