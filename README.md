# CharlotteChenResume

app.py - contains actual flask app that initiates program, the first module that is called.
config.py - connects flask app to sqlite3 database by declaring the path to the db_file.db file
db_create.py - creates the database in a file called db_file.db
templates - these are the actual html files that construct the layout of the page 'file.html'
models - contains data for structure and creation of database tables, data manipulation, and data pulls
views - handles front-end/which template and data to return from the templates and models folder. Each url links to a function that returns
       a specific template and it's corresponding data from a model
static - contains files like javascript, stylesheets, and images

Each page will have its own template, javascript, stylesheet, model, and view


Querying Database through console
---------------------------------
Dashboard -> Consoles -> Bash
1) cd to mysite path
2) enter 'sqlite3 db_file.db'
3) run sql queries


Add git to local machine
-----------------------------------
1) git init
2) git add README.md
3) git commit -m "first commit"
4) git remote add origin https://github.com/dth26/Weather-Map.git
5) git push -u origin master

Push modified code to master
------------------------------------
1) git add templates/base.html
2) git commit -m "update base.html page"
3) git push -u origin master

Pull modified code from master
----------------------------------
1) git pull origin master
