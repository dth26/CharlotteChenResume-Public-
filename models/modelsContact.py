import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/')

from sqlalchemy import *
from __init__ import db
from sqlalchemy.orm import relationship, backref
from flask import request, session
from app import app
import os


class Messages(db.Model):
	__tablename__ = 'Messages'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	messageID = Column(Integer, primary_key = True)
	sender = Column(Integer, ForeignKey('School.schoolID'), nullable = False)
	subject = Column(String)
	message = Column(String)

	def __init__(self, messageID, sender, subject, message):
		self.messageID = messageID
		self.sender = sender
		self.subject = subject
		self.message = message


def insertMessage(sender,subject,message):
	# connect to database
	engine = create_engine('sqlite:///' + os.path.join(basedir, 'db_file.db'), echo=True)
	connection = engine.connect()

	query = text('INSERT INTO Messages(`sender`,`subject`,`message`) VALUES(:sender, :subject, :message)')
	connection.execute(query,  sender = sender, subject = subject, message = message)
	connection.close()