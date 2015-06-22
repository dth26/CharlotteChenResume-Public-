

#	main.py application creates object (of class Flask)
#	imports views

from flask import Flask                    # import Flask library from flask package

app = Flask(__name__)

# add models and views folder to path
#import sys
#sys.path.insert(0, '/var/www/html/Charlotte/main/views/')
#sys.path.insert(0, '/var/www/html/Charlotte/main/models/')


# must import all views called in application
from viewIndex import *
from viewCode import *
from viewArt import *
from userLog import *
from viewContact import *
from viewAbout import *


#wsgi_app = app.wsgi_app 		# Make the WSGI interface at the top level so wfastcgi can get it