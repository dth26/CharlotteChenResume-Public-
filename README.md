# CharlotteChenResume

MODIFYING SITE
===========================================================================================
NOTE: make sure you cd to to right directory (dev or mysite) in bash  when pushing or pulling from git
-   There are two sites; one for testing/modifying dev and one for final production
-   All modifications should first be tested in dev website
        1)  before modifying dev set pull from master or else repository will be behind
-   After modifications are tested and work properly in dev site
        1)  push code from dev branch to master
        2)  pull code from master to production site

-   Dev
        URL:        http://pythonprogrammer.pythonanywhere.com/index/
        PATH:       /home/pythonprogrammer/dev
        GIT BRANCH: dev
-   Production
        URL:        meetcharlottechen.com
        PATH:       /home/pythonprogrammer/mysite
        GIT BRANCH: origin


FILES
===========================================================================================

app.py          - contains actual flask app that initiates program, the first module that is called.
config.py       - connects flask app to sqlite3 database by declaring the path to the db_file.db file
db_create.py    - creates the database in a file called db_file.db
__init__.py     - contains connection to database called 'db'. Must be imported by all models
templates       - these are the actual html files that construct the layout of the page 'file.html'
models          - contains data for structure and creation of database tables, data manipulation, and data pulls.
                    a) Any new models should be imported into models.py
views           - handles front-end/which template and data to return from the templates and models folder. Each url links to a function that returns
                  a specific template and it's corresponding data from a model.
                    a) Any new views should be imported into app.py
                    b) All views must have session api key
                    c) All views must return user = session data to template
static - contains files like javascript, stylesheets, and images

Each page will have its own template, javascript, stylesheet, model, and view


QUERYING DATABASE THROUGH BASH
=============================================================================================
Dashboard -> Consoles -> Bash
1) cd to mysite path
2) enter 'sqlite3 db_file.db'
3) run sql queries


CREATE NEW BRANCH ON GIT
=============================================================================================
1) git init
2) git add README.md
3) git commit -m "first commit"
4) git remote add origin https://github.com/dth26/Weather-Map.git
5) git push -u origin master


PUSH MODIFIED CODE TO MASTER
=============================================================================================
1) git add templates/base.html
2) git commit -m "update base.html page"
3) git push -u origin master


PULL MODIFIED CODE FROM MASTER
=============================================================================================
1) git pull origin master



Overwrite local branch with master
-------------------------------
1) git fetch --all
2) git reset --hard origin/master

