
from flask import render_template, request, session, redirect, url_for



@app.route('/login', methods=['GET', 'POST'])
def login():
	name = request.form.get('name')
	password = request.form.get('password')


	#if request.method == 'POST':
	user = Users.query.filter_by(firstName=name);


	if user.count() > 0 and user[0].password==password:
		session['username'] = user[0].firstName
		session['lastName'] = user[0].lastName
		session['privileges'] = user[0].privileges
		session['city'] = user[0].city
		session['state'] = user[0].state
	else:
		session.pop('username', None)

	return render_template('index.html', page='index',  user = session)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'