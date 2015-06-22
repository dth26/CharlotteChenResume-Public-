import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/models')

import smtplib

from modelsContact import *
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template, request, session

@app.route('/contact')
def contact():
	return render_template('contact/contact.html', user = session);

@app.route('/contact/sent',  methods=['GET', 'POST'])
def sent():
	message = request.form['message']
	sender = request.form['from']
	subject = request.form['subject']
	receiver = "danielhui123@gmail.com"
	returnMessage = ""

	username = "danielhui123@gmail.com"
	password  = "@zxcvbnm4"


	# save data in contacts table
	insertMessage(sender, subject, message)


	# send email to user
	try:	# sucessful message request

		text = """Subject: %s ----- %s """ % (subject, message)  
		returnMessage = "Message Sent Sucessfully to " + receiver + "!"

		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(sender, receiver, text)
		server.quit()
	except:
		returnMessage = "Message failed to send to " + receiver +"."
	
	return render_template('contact/sent.html', user = session, returnMessage = returnMessage)



