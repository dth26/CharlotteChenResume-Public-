# CharlotteChenResume

app.py - contains actual flask app that initiates program, the first module that is called.
config.py - connects flask app to sqlite3 database by declaring the path to the db_file.db file
db_create.py - creates the database in a file called db_file.db 
templates - these are the actual html files that construct the layout of the page 'file.html'
models - contains data for structure and creation of database tables, data manipulation, and data pulls
views - handles front-end/which template and data to return from the templates and models folder. Each url links to a function that returns 
       a specific template and it's corresponding data from a model
static - contains files like javascript, stylesheets, and images


Querying Database through console
---------------------------------
1) cd to mysite path
2) enter 'sqlite3 db_file.db'
3) run sql queries
