

#	main.py application creates object (of class Flask)
#	imports views

from flask import Flask, session                    # import Flask library from flask package

app = Flask(__name__)



# must import all views called in application
from viewIndex import *
from viewCode import *
from viewArt import *
from userLog import *
from viewContact import *
from viewAbout import *




#wsgi_app = app.wsgi_app 		# Make the WSGI interface at the top level so wfastcgi can get it