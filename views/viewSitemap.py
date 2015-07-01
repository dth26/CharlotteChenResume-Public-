from app import app
# invokes the Jinja2 templating engine . Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments
from flask import render_template


#	respond to request form web server
#	each function maps to a request url



@app.route('/sitemap.xml')
@app.route('/sitemap.xml/')
def index():
	return render_template('sitemap.xml')





