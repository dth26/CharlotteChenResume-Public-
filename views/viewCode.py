
from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template, session
from modelsCode import *
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import *
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# configure Session class with desired options


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db_file.db')		# path of db file

# an Engine, which the Session will use for connection
# resources
engine = create_engine(SQLALCHEMY_DATABASE_URI)


session.configure(bind=engine)
'''

@app.route('/code/')
@app.route('/code')
def code():
	userData = getUserData()
	schools = getSchools()
	majors = getMajors()
	courses = getCourses()
	skills = getSkills()
	companies = getCompanies()
	companyDescriptions = getCompanyDescriptions()

	return render_template('code/code.html',
							user = session,
							userData = userData,
							schools = schools,
							majors = majors,
							courses = courses,
							skills = skills,
							companies = companies,
							companyDescriptions = companyDescriptions,
							subpage = "all");


@app.route('/code/education/')
@app.route('/code/education')
def Education():
	userData = getUserData()
	schools = getSchools()
	majors = getMajors()
	return render_template('code/code.html',
							user = session,
							userData = userData,
							schools = schools,
							majors = majors,
							subpage = "education")


@app.route('/code/courses/')
@app.route('/code/courses')
def Courses():
	userData = getUserData()
	courses = getCourses()
	schools = getSchools()
	majors = getMajors()
	return render_template('code/code.html',
							user = session,
							userData = userData,
							schools = schools,
							majors = majors,
							courses = courses,
							subpage = "courses")


@app.route('/code/experience/')
@app.route('/code/experience')
def Experience():
	userData = getUserData()
	courses = getCourses()
	schools = getSchools()
	majors = getMajors()
	companies = getCompanies()
	companyDescriptions = getCompanyDescriptions()
	return render_template('code/code.html',
							user = session,
							userData = userData,
							schools = schools,
							majors = majors,
							companies = companies,
							companyDescriptions = companyDescriptions,
							subpage = "experience");


@app.route('/code/skills/')
@app.route('/code/skills')
def Skills():
	userData = getUserData()
	courses = getCourses()
	schools = getSchools()
	majors = getMajors()
	skills = getSkills()
	return render_template('code/code.html',
							user = session,
							userData = userData,
							schools = schools,
							majors = majors,
							skills = skills,
							subpage = "skills");


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'