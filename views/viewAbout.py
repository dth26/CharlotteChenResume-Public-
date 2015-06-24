from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template, session
from modelsAbout import *

@app.route('/about')
@app.route('/about/')
def about():
	# get descriptions
	descMe = getAboutDescriptions("me")
	facts = getAboutDescriptions("fact")
	likes = getAboutDescriptions("like")
	descTravel = getAboutDescriptions("travel")
	descFashion = getAboutDescriptions("fashion")
	descDrawing  = getAboutDescriptions("drawing")
	descriptions = getAboutDescriptions("")

	# get photos
	imagesMe = getAboutPhotos("main")
	imagesLikes = getAboutPhotos("about")
	imagesFashion = getAboutPhotos("fashion")
	imagesTravel = getAboutPhotos("travel")
	imagesDrawings = getAboutPhotos("drawing")
	photos =  getAboutPhotos("")

	return render_template('about/about.html',
				descriptions=descriptions,
				descMe=descMe,
				facts=facts,
				likes=likes,
				descTravel=descTravel,
				descFashion=descFashion,
				descDrawing=descDrawing,
				imagesLikes = imagesLikes,
				imagesMe = imagesMe,
				photos = photos,
				imagesTravel = imagesTravel,
				imagesDrawings= imagesDrawings,
				imagesFashion = imagesFashion,
				user = session);

# set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'