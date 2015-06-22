#!/var/www/html/Charlotte/Flask/venv/bin/python


# starts the web server

from app import app


# launching server
# http://127.0.0.1:5001/
# http://127.0.0.1:5001/index
#app.run(host='127.0.0.1', debug=True, port=5008, use_reloader=True)
app.run(debug=True)