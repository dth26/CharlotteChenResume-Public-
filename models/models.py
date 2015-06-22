import sys
sys.path.insert(0, '/var/www/html/Charlotte/main/models')
sys.path.insert(0, '/var/www/html/Charlotte/main/')

#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import *
#from sqlalchemy.dialects import mysqldef
from __init__ import db
from sqlalchemy import *

# import ALL models
from modelsCode import *
from modelsArt import *
from modelsAbout import *



# automatically called and creates tables when db_create is called
# if new table is added simply call 'python models.py'
# after new table is added insert '__table_args__ = {'extend_existing': True}' to ensure table will not try to be built again

# our database tables are represented using classes



class Users(db.Model):
	__tablename__ = 'Users'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	userID = Column(Integer, primary_key = True)
	password = Column(String)
	privileges = Column(Integer)
	firstName = Column(String)
	lastName = Column(String)
	city = Column(String)
	state = Column(String)
	phone = Column(Integer)
	email = Column(String)

	def __init__(self, userID, password, privileges, firstName, lastName, city, state, phone, email):
		self.userID = userID
		self.password = password
		self.privileges = privileges
		self.firstName = firstName
		self.lastName = lastName
		self.city = city
		self.state = state
		self.phone = phone;
		self.email = email;




class Pages(db.Model):
	__tablename__ = 'Pages'
	__table_args__ = {'extend_existing': True}			# ONLY IF TABLE ALREADY EXISTS IN DATABASE

	pageId = Column(Integer, primary_key = True)
	name = Column(String)	# art, code, graphics, layouts, logos, about
	description = Column(String)
	img = Column(String)

	def __init__(self, pageId, name, description, img):
		self.pageId = pageId
		self.name = name
		self.description = description
		self.img = img


# Initialize database schema (create tables)
db.create_all()




def getUserData():
	userData = Users.query.all()
	return userData



'''
command line
----------------
-> python
-> from __init__ import db
-> import models
->	u = models.Users(None, password = "Naruto", privileges = 1, firstName = "Charlotte",
	lastName = "Chen", city = "Pittsburgh", state = "Pa", phone = 2155799999)
-> db.session.add(user)
-> db.session.commit()			// save results
-> users = models.Users.query.all()
-> users
-> for u in users:
...    print(u.userId,u.password)
-> users = models.Users.query.get(1)
-> users
'''


'''
ALTERING TABLE with database file 'ncaaf.db' and table games

sqlite3 ncaaf.db
alter table games add column q4 type float

'''