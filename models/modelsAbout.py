import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/')

from __init__ import db
from sqlalchemy import *
from app import app
from flask import request, url_for, render_template, redirect

from sqlalchemy.engine import create_engine
import os


basedir = "/var/www/html/Charlotte/main/"

	
class imagesAbout(db.Model):
	__tablename__ = 'imagesAbout'
	_table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	imageID = Column(Integer, primary_key = True)
	idName = Column(String)								# used for identifying div
	description = Column(String)
	imageType = Column(String) 	# Layouts, Graphics, Logos, Drawings
	path = Column(String)

	def __init__(self,imageID, idName, description, imageType, path):
		self.idName = idName									
		self.imageID = imageID
		self.description = description
		self.imageType = imageType
		self.path = path


class descriptionsAbout(db.Model):
	__tablename__ = 'descriptionsAbout'
	_table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	descID = Column(Integer, primary_key = True)
	descType = Column(String)							# list will have multiple entries
	idName = Column(String)
	description = Column(String)

	def __init__(self, descID, descType, idName, description):
		self.descID = descID
		self.descType = descType
		self.idName = idName
		self.description = description

@app.route('/about/newAboutDescription', methods=['GET', 'POST'])
def newAboutDescription():
	if request.method != 'POST':
		return redirect(url_for('about'))
	
	idName = request.form['idName']
	description = request.form['description']
	descType = request.form['descType']
	
	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	query = text('INSERT INTO descriptionsAbout(`idName`,`description`,`descType`) VALUES(:idName, :description, :descType)')
	connection.execute(
		query,
		idName = idName,
		description = description,
		descType = descType)
	connection.close()
	return redirect(url_for('about'))
	
		
@app.route('/about/newAboutPhoto', methods=['GET', 'POST'])
def newAboutPhoto():
	if request.method != 'POST':
		return redirect(url_for('about'))

	idName = request.form['idName']
	description = request.form['description']
	imageType = request.form['imageType']


	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	# upload file to system
	# Get the name of the uploaded file
	file = request.files['file']
	# Check if the file is one of the allowed types/extensions
	if file:
	# Make the filename safe, remove unsupported chars
		filename = file.filename
		# compute location to save photo
		uploaddir = basedir + "/static/images/about" + filename
	# Move the file form the storage location
		file.save(uploaddir)

	query = text('INSERT INTO imagesAbout(`idName`,`description`,`imageType`,`path`) VALUES(:idName, :description, :imageType, :path)')
	connection.execute(
		query,
		idName = idName,
		description = description,
		path = file.filename,
		imageType = imageType)
	connection.close()
	return redirect(url_for('about'))


@app.route('/about/editAboutPhoto', methods=['GET', 'POST'])
def editAboutPhoto():
	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()
	# get new photo data
	imageID = request.form['imageID']
	idName = request.form['idName']
	description = request.form['description']
	imageType = request.form['imageType']

	if description != "":
		updatePhotoDescription("description", description, imageID, connection)
	if idName != "":
		updatePhotoID(idName, imageID, connection)
	if imageType != "":
		updatePhotoType(imageType, imageID, connection)
	
			
	connection.close()
	return redirect(url_for('about'))


@app.route('/about/editAboutDescription', methods=['GET', 'POST'])
def editAboutDescription():
	descID = request.form['descID']
	idName = request.form['idName']
	description = request.form['description']
	descType = request.form['descType']
	
	if idName != "":
		updateDescriptionidName(idName, descID, connection)
	if description != "":
		updateDescriptionDescription(description, descID, connection)
	if descType != "":
		updateDescriptionType(descType, descID, connection)
			
	connection.close()
	return redirect(url_for('about'))
	
	
def updateDescriptionidName(value, descID, connection):
	query = text('UPDATE descriptionsAbout SET idName=:value WHERE descID == :descID')
	connection.execute(
		query,
		value = value,
		descID = descID)

def updateDescriptionDescription(value, descID, connection):
	query = text('UPDATE descriptionsAbout SET description=:value WHERE descID == :descID')
	connection.execute(
		query,
		value = value,
		descID = descID)

def updateDescriptionType(value, descID, connection):
	query = text('UPDATE descriptionsAbout SET descType=:value WHERE descID == :descID')
	connection.execute(
		query,
		value = value,
		descID = descID)



def updatePhotoType(value, imageID, connection):
	query = text('UPDATE imagesAbout SET imageType=:value WHERE imageID == :imageID')
	connection.execute(
		query,
		value = value,
		imageID = imageID)	

def updatePhotoID(value, imageID, connection):
	query = text('UPDATE idName SET idName=:value WHERE imageID == :imageID')
	connection.execute(
		query,
		value = value,
		imageID = imageID)	

def updatePhotoDescription(value, imageID, connection):
	query = text('UPDATE idName SET idName=:value WHERE imageID == :imageID')
	connection.execute(
		query,
		value = value,
		imageID = imageID)	


	
def getAboutDescriptions(type):
	if(type == ""):
		descriptions = descriptionsAbout.query.all()
	else:
		descriptions = descriptionsAbout.query.filter_by(descType=type)
	return descriptions

def getAboutPhotos(type):
	if(type == ""):
		photos = imagesAbout.query.all()
	else:
		photos = imagesAbout.query.filter_by(imageType=type)
	return photos


@app.route('/about/deleteAboutPhoto', methods=['GET', 'POST'])
def deleteAboutPhoto():
	imageId = request.form['imageId']
	query = text('DELETE FROM imagesAbout WHERE imageId==:imageId')

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	connection.execute(
		query,
		imageId = imageId)

	return redirect(url_for('about'))


@app.route('/about/deleteAboutDescription', methods=['GET', 'POST'])
def deleteAboutDescription():
	descID = request.form['descID']
	query = text('DELETE FROM descriptionsAbout WHERE descID==:descID')

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	connection.execute(
		query,
		descID = descID)

	return redirect(url_for('about'))