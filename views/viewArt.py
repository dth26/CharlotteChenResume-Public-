import sys
sys.path.insert(0,'var/www/html/Charlotte/main/models')

from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template, request, session
from modelsArt import *

@app.route('/art/')
@app.route('/art')
def art():
	return render_template('art/art.html', subpage = "ArtMain", user = session);

@app.route('/art/layouts/')
@app.route('/art/layouts')
def Layouts():
	photos = getPhotos("Layouts")
	return render_template('art/layouts.html', photos = photos , subpage = "Layouts", user = session);


@app.route('/art/graphics/')
@app.route('/art/graphics')
def Graphics():
	photos = getPhotos("Graphics")
	return render_template('art/layouts.html', photos = photos ,subpage = "Graphics",  user = session);

@app.route('/art/logos/')
@app.route('/art/logos')
def Logos():
	photos = getPhotos("Logos")
	return render_template('art/layouts.html', photos = photos ,subpage = "Logos", user = session);



@app.route('/art/drawings/')
@app.route('/art/drawings')
def Drawings():
	photos = getPhotos("Drawings")
	return render_template('art/layouts.html', photos = photos ,subpage = "Drawings", user = session);


def getPhotos(type):
	photos = Images.query.filter_by(imageType=type);
	return photos





# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'