import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/')
sys.path.insert(0, '/var/www/html/Charlotte/main/models')

from sqlalchemy import *
from __init__ import db
from models import *
from sqlalchemy.orm import relationship, backref
from flask import request, url_for, render_template, redirect, session
from app import app
import os


basedir = "/home/pythonprogrammer/mysite/"




# school
class School(db.Model):
	__tablename__ = 'School'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	schoolID = Column(Integer, primary_key = True)
	userID = Column(Integer, nullable=False )
	school = Column(String, nullable = False)
	startDate = Column(String)
	endDate = Column(String)
	year = Column(String)
	order = Column(Integer)

	def __init__(self, schoolID, userID, school, startDate, endDate, year, order):
		self.schoolID = schoolID
		self.userID = userID
		self.school = school
		self.startDate = startDate
		self.endDate = endDate
		self.order = order
		self.year = year


# major
class Major(db.Model):
	__tablename__ = 'Major'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	majorID = Column(Integer, primary_key = True)
	schoolID = Column(Integer, ForeignKey('School.schoolID'), nullable = False)
	major = Column(String)
	degree = Column(String)								# Graduate's, Bachelor's

	def __init__(self, majorID, schoolID, major, degree):
		self.majorID = majorID
		self.schoolID = schoolID
		self.major = major
		self.degree = degree


#courses
class Course(db.Model):
	__tablename__ = 'Course'
	__table_args__ = {'extend_existing': True}

	courseID = Column(Integer, primary_key = True)
	userID = Column(Integer)
	majorID = Column(Integer)
	course = Column(String)
	description = Column(String)


	def __init__(self, courseID, userID, majorID, course, description):
		self.courseID = courseID
		self.userID = userID
		self.majorID = majorID
		self.course = course
		self.description = description




# skills
class Skill(db.Model):
	__tablename__ = 'Skill'
	__table_args__ = {'extend_existing': True}

	skillID = Column(Integer, primary_key = True)
	majorID = Column(Integer, autoincrement = True)
	skill = Column(String)
	years = Column(Integer)
	order = Column(Integer, autoincrement = True)

	def __init__(self,skillID,majorID,skill,years,order):
		self.skillID = skillID
		self.majorID = majorID
		self.skill = skill
		self.years = years
		self.order = order

# company
class Company(db.Model):
	__tablename__ = 'Company'
	__table_args__ = {'extend_existing': True}

	companyID = Column(Integer, primary_key = True)
	startDate = Column(String)
	endDate = Column(String)
	company = Column(String)
	position = Column(String)
	state = Column(String)
	city = Column(String)

	def __init__(self, companyID, startDate, endDate, company, position, state, city):
		self.companyID = companyID
		self.startDate = startDate
		self.endDate = endDate
		self.company = company
		self.position = position
		self.state = state
		self.city = city

# company descriptions
class CompanyDescription(db.Model):
	__tablename__ = 'CompanyDescription'
	__table_args__ = {'extend_existing': True}

	companyDescriptionID = Column(Integer, primary_key = True)
	companyID = Column(Integer)
	description = Column(String)

	def __init__(self, companyDescriptionID, companyID, description):
		self.companyDescriptionID = companyDescriptionID
		self.companyID = companyID
		self.description = description


# Initialize database schema (create tables)
db.create_all()




# get school data
def getSchools():
	schools = School.query.all()
	return schools

def getMajors():
	majors = Major.query.all()
	return majors

def getCourses():
	courses = Course.query.all()
	return courses

def getSkills():
	skills = Skill.query.order_by("years desc")
	return skills

def getCompanies():
	companies = Company.query.all()
	return companies

def getCompanyDescriptions():
	descriptions = CompanyDescription.query.all()
	return descriptions



# user functions
@app.route('/code/editCourse', methods=['GET','POST'])
def editCourse():
	if request.method != 'POST':
		return redirect(url_for('code'))

	# get form inputs
	description = request.form['description']
	courseID = request.form['courseID']
	course = request.form['course']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()


	query = text('UPDATE Course SET description=:description WHERE courseID==:courseID')
	connection.execute(query, courseID = courseID, description = description)

	query = text('UPDATE Course SET course=:course WHERE courseID==:courseID')
	connection.execute(query, course=course, courseID=courseID)

	connection.close()

	return redirectURL('course')


@app.route('/code/editCompany', methods=['GET','POST'])
def editCompany():
	if request.method != 'POST':
		return redirect(url_for('code'))

	# get form inputs
	company = request.form['company']
	start = request.form['start']
	end = request.form['end']
	position = request.form['position']
	state = request.form['state']
	city = request.form['city']
	companyID = request.form['dataID']


	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	if company != "":
		query = text('UPDATE Company Set company=:company WHERE companyID==:companyID')
		connection.execute(query, company = company, companyID = companyID)
	if start != "":
		query = text('UPDATE Company Set startDate=:start WHERE companyID==:companyID')
		connection.execute(query, start = start, companyID = companyID)
	if end != "":
		query = text('UPDATE Company Set endDate=:end WHERE companyID==:companyID')
		connection.execute(query, end = end, companyID = companyID)
	if position != "":
		query = text('UPDATE Company Set position=:position WHERE companyID==:companyID')
		connection.execute(query, position = position, companyID = companyID)
	if state != "":
		query = text('UPDATE Company Set state=:state WHERE companyID==:companyID')
		connection.execute(query, state = state, companyID = companyID)
	if city != "":
		query = text('UPDATE Company Set city=:city WHERE companyID==:companyID')
		connection.execute(query, city = city, companyID = companyID)

	connection.close()

	return redirectURL('experience')

@app.route('/code/editCompanyDescription', methods=['GET','POST'])
def editCompanyDescription():
	if request.method != 'POST':
		return redirect(url_for('code'))

	# get form input
	companyID = request.form['dataID']
	description = request.form['description']


	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	query = text('UPDATE CompanyDescription SET description=:description WHERE companyID=:companyID')
	connection.execute(query, description=description, companyID=companyID)
	connection.close()

	return redirectURL('experience')




# user functions
@app.route('/code/editSchool', methods=['GET','POST'])
def editSchool():
	if request.method != 'POST':
		return redirect(url_for('education'))

	# get form inputs
	school = request.form['school']
	start = request.form['start']
	end = request.form['end']
	schoolID = request.form['dataID']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	if school != "":
		query = text('UPDATE School SET school=:school WHERE schoolID==:schoolID')
		connection.execute(query, schoolID = schoolID, school = school)
	if start != "":
		query = text('UPDATE School SET startDate=:start WHERE schoolID==:schoolID')
		connection.execute(query, start=start, schoolID=schoolID)
	if end != "":
		query = text('UPDATE School SET endDate=:end WHERE schoolID==:schoolID')
		connection.execute(query, end=end, schoolID=schoolID)

	connection.close()

	return redirectURL('education')



@app.route('/code/editSkill', methods=['GET','POST'])
def editSkill():
	if request.method != 'POST':
		return redirect(url_for('skill'))

	skill = request.form['skill']
	skillID = request.form['dataID']
	years = request.form['years']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	if skill != "":
		query = text('UPDATE Skill SET skill=:skill WHERE skillID==:skillID')
		connection.execute(query,skill=skill, skillID=skillID)
	if years != "":
		query = text('UPDATE Skill SET years=:years WHERE skillID==:skillID')
		connection.execute(query,years=years,skillID = skillID)

	connection.close()
	return redirectURL('skill')


@app.route('/code/insertData', methods=['GET','POST'])
def insertData():
	if request.method != 'POST':
		return redirect(url_for('code'))

	# figure which table to insert into
	section = request.form['section']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()


	if section == "Insert Course":
		# get form input
		majorID = request.form['major']
		description = request.form['description']
		course = request.form['course']
		query = text('INSERT INTO Course(`userID`,`majorID`,`description`,`course`) VALUES(:userID,:majorID, :description, :course)')
		connection.execute(query, userID = 1, description = description, majorID = majorID, course = course)
		connection.close()
		return redirectURL('course')
	elif section == "Insert School":
		# get form input
		school = request.form['school']
		start = request.form['start']
		end = request.form['end']
		query = text('INSERT INTO School(`userID`,`startDate`,`endDate`,`school`) VALUES(:userID,:start,:end,:school)')
		connection.execute(query, userID = 1, start = start, end = end, school = school)
		connection.close()
		return redirectURL('education')
	elif section == "Insert Company":
		# get form input
		company = request.form['company']
		start = request.form['start']
		end = request.form['end']
		position = request.form['position']
		state = request.form['state']
		city = request.form['city']
		query = text('INSERT INTO Company(`company`,`startDate`,`endDate`,`position`,`state`,`city`) VALUES(:company,:start,:end,:position,:state,:city)')

		if company!="" and start!="" and end!="" and position!="" and state!="" and city!="":
			connection.execute(query, company = company, start = start, end = end, position = position, state = state, city = city)

		connection.close()
		return redirectURL('experience')
	elif section == "Insert Company Description":
		# get form input
		description = request.form['description']
		companyID = request.form['companyID']
		query = text('INSERT INTO CompanyDescription(`companyID`,`description`) VALUES(:companyID,:description)')

		if description!= "" and companyID!= "":
			connection.execute(query, description = description, companyID = companyID)

		connection.close()
		return redirectURL('experience')
	elif section == "Insert Skill":
		# get form input
		skill = request.form['skill']
		years = request.form['years']

		query = text('INSERT INTO Skill(`skill`,`years`,`majorID`) VALUES(:skill,:years,:major)')

		if skill != "" and years != "":
			connection.execute(query,skill=skill, years=years, major=1)

		connection.close()
		return redirectURL('skill')


@app.route('/code/deleteData', methods=['GET','POST'])
def deleteData():
	if request.method != 'POST':
		return redirect(url_for('code'))

	# get form input
	section = request.form['section']
	dataID = request.form['dataID']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()


	if section == "Delete Course":
		query = text('DELETE FROM Course WHERE courseID=:courseID')
		connection.execute(query, courseID = dataID)
		connection.close()
		return redirectURL('course')
	elif section == "Delete School":
		query = text('DELETE FROM School WHERE schoolID=:schoolID')
		connection.execute(query, schoolID = dataID)
		connection.close()
		return redirectURL('education')
	elif section == "Delete Company":
		# delete company
		query = text('DELETE FROM Company WHERE companyID=:companyID')
		connection.execute(query, companyID = dataID)
		# delete descriptions
		query = text('DELETE FROM CompanyDescription WHERE companyID=:companyID')
		connection.execute(query, companyID = dataID)
		connection.close()
		return redirectURL('experience')
	elif section == "Delete Skill":
		query = text('DELETE FROM Skill WHERE skillID=:skillID')
		connection.execute(query, skillID=dataID)
		return redirectURL('skill')



def redirectURL(section):
	redirect_function = ""
	if section == 'course':
		redirect_function = "Courses"
	elif section == 'skill':
		redirect_function = "Skills"
	elif section == 'experience':
		redirect_function = "Experience"
	elif section == 'education':
		redirect_function = "Education"

	return redirect(url_for(redirect_function))



# get school data
def getSchools():
	schools = School.query.all()
	return schools

def getUserData():
	userData = Users.query.all()
	return userData

def getMajors():
	majors = Major.query.all()
	return majors

def getCourses():
	courses = Course.query.all()
	return courses

def getSkills():
	skills = Skill.query.order_by("years desc")
	return skills

def getCompanies():
	companies = Company.query.all()
	return companies

def getCompanyDescriptions():
	descriptions = CompanyDescription.query.all()
	return descriptions