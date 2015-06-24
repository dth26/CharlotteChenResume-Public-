
from __init__ import db
from sqlalchemy import *
from app import app
from flask import request, url_for, render_template, redirect

from sqlalchemy.engine import create_engine
import os

basedir = "/home/pythonprogrammer/mysite/"


# images table for art page
class Images(db.Model):
	__tablename__ = 'Images'
	_table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	imageID = Column(Integer, primary_key = True)
	idName = Column(String)								# used for identifying divs
	title = Column(String)
	description = Column(String)
	imageType = Column(String) 	# Layouts, Graphics, Logos, Drawings
	path = Column(String)

	def __init__(self,imageID, idName, title, description, imageType, path):
		self.idName = idName
		self.imageID = imageID
		self.title = title
		self.description = description
		self.imageType = imageType
		self.path = path


# delete a photo
# note this does not delete photo on server, only deletes record in table
@app.route('/art/deletePhoto', methods=['GET', 'POST'])
def deletePhoto():
	imageId = request.form['imageId']
	query = text('DELETE FROM Images WHERE imageId==:imageId')

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	connection.execute(
		query,
		imageId = imageId)

	return redirect(url_for('Layouts'))

# create a new photo
@app.route('/art/newPhoto', methods=['GET', 'POST'])
def newPhoto():

	if request.method != 'POST':
		return redirect(url_for('Layouts'))

	# get new photo data
	title = request.form['title']
	idName = request.form['id']
	description = request.form['description']
	imageType = request.form['imageType']

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	# compuete where to save image
	imageSubfolder = ""
	if imageType == "Layouts":
		imageSubfolder = "/layouts/"
	elif imageType == "Graphics":
		imageSubfolder = "/graphics/"
	elif imageType == "Drawings":
		imageSubfolder = "/drawings/"
	elif imageType == "Logos":
		imageSubfolder = "/logos/"


	# upload file to system
	# Get the name of the uploaded file
	file = request.files['file']
    # Check if the file is one of the allowed types/extensions
	if file:
        # Make the filename safe, remove unsupported chars
		filename = file.filename
		# compute location to save photo
		uploaddir = basedir + "/static/images" + imageSubfolder + filename
        # Move the file form the storage location
		file.save(uploaddir)


	query = text('INSERT INTO Images(`title`,`idName`,`description`,`imageType`,`path`) VALUES(:title, :idName, :description, :imageType, :path)')
	connection.execute(
                  query,
                  title = title,
                  idName = idName,
                  description = description,
                  path = imageSubfolder + file.filename,
                  imageType = imageType)

	connection.close()

	return redirect(url_for('Layouts'))


# edit photo
@app.route('/art/editPhoto', methods=['GET', 'POST'])
def editPhoto():

	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	# get new photo data
	imageId = request.form['imageId']
	title = request.form['title']
	idName = request.form['id']
	description = request.form['description']
	imageType = request.form['imageType']
	path = request.form['path']

	if description != "":
		updateDescription(description, imageId, connection)

	if title != "":
		updateTitle(title, imageId, connection)

	if idName != "":
		updateIdName(idName, imageId, connection)

	if imageType != "":
		updateImageType(imageType, imageId, connection)

	if path != "":
		updatePath(path, imageId, connection)


	connection.close()

	return redirect(url_for('Layouts'))


# called by editPhoto
# edit title
def updateTitle(title, imageId, connection):
	query = text('UPDATE Images SET title=:title WHERE imageID == :imageId')
	connection.execute(
                  query,
                  title = title,
                  imageId = imageId)


# called by editPhoto
# edit description
def updateDescription(description, imageId, connection):
	query = text('UPDATE Images SET description =:description WHERE imageID == :imageId')
	connection.execute(
                  query,
                  description = description,
                  imageId = imageId)


# called by editPhoto
# edit path
def updatePath(path, imageId, connection):
	query = text('UPDATE Images SET path=:path WHERE imageID == :imageId')
	connection.execute(
                  query,
                   imageId = imageId,
                  path = path)

# called by editPhoto
# edit idName
def upateIdName(idName, imageId, connection):
	query = text('UPDATE Images SET idName =:idName WHERE imageID == :imageId')
	connection.execute(
                  query,
                  imageId = imageId,
                  idName = idName)

# called by editPhoto
# edit imageType
def updateImageType(imageType, imageId, connection):
	query = text('UPDATE Images SET imageType =:imageType WHERE imageID == :imageId')
	connection.execute(
                  query,
                  imageId = imageId,
                  imageType = imageType)



# return photos of type(drawings, logos, graphics, layouts)
def getPhotos(type):
	photos = Images.query.filter_by(imageType=type);
	return photos




