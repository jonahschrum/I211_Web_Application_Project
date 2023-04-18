from flask import Flask, render_template, url_for, request, redirect
import csv
import html
from os.path import exists

app = Flask(__name__)


app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')


#allows access to mysql

import database



# Sets courses.csv as source of data to reference in URL pages.

COURSE_PATH = app.root_path + '/courses.csv'
COURSE_KEYS = ['ID', 'Name', 'Pet_Type', 'Level','Start_Date', 'Start_Time', 'Course_Duration', 'Course_Length', 'Trainer', 'Description']


#index function brings user to home page, which simpy renders index.html, using
# the '/' route.

@app.route('/')
def index():
    return render_template('index.html')



# course_list function retrieves data from get_courses function and then
# creates the course_list.html page. The data can be referenced there by the
# variable added_courses. This function now receives ALL the data using the 
# get_courses function in database.py REGARDLESS of the course_id, meaning 
# it will grab all of them. This is then rendered on the course_list page,
# and formated in course_list.html.

@app.route('/courses/')
def course_list():  
    courses=database.get_courses()
    return render_template('course_list.html', courses=courses)




# This function now fetches the data from sql using the get_course function in 
# database.py to extract the information by calling for the course_id. Then, the
# info is rendered in course.html.

@app.route('/courses/<course_id>')
def course(course_id=None):
    if course_id:
        course_id=int(course_id)
        course = database.get_course(course_id)
        return render_template('course.html', course=course)
    else:
        pass



# This function creates the /courses/create route which allows the user
# to access a form which inputs new data for a course. The function pulls 
# all the data input on add_course.html using request.form, and then adds it 
# to the new_course dictionary. After added, the ID of the new course is
# set to a variable which add the new course into the function set_courses,
# which bascically adds the new entries back into courses.csv. After they are
# added, get_courses pulls all the courses back into course_list, which shows 
# the updated courses on the website. It has been modified to run into database.py
# using database, and plugs all the variables into the function add course, 
# thereby adding data to the course table in mysql. 


@app.route('/courses/create', methods=['GET', 'POST'])
def new_course():
    if request.method == 'POST':
        print('clicked submit')
        new_course = {}
        name=request.form['Name']
        pet_type=request.form['Pet_Type']
        level=request.form['Level']
        start_date=request.form['Start_Date']
        start_time=request.form['Start_Time']
        course_duration=request.form['Course_Duration']
        course_length=request.form['Course_Length']
        trainer=request.form['Trainer']
        description=request.form['Description']
        database.add_course(name, pet_type, level, start_date, start_time, course_duration, course_length, trainer, description)
        return redirect(url_for('course_list'))
    else:   
        return render_template('add_course.html')
    

# This function navigates the user to edit a course that has been previously
# added, I could not figure out how to make this work. I tried using
# a jinja if statement in course_list by calling a variable but it did not work.
# This is something I will have to be sure to figure out/understand in the future. 
# This function works the same way as create, except it goes to the update_course
# function in database.py, thereby maintaining the same data and just adding in where
# inputs have been edited. The fate as to whether a form is edited or new is decieded
# on the add_course.html page, where a jinja if statement switches the paths. 

@app.route('/courses/<course_id>/edit', methods=['GET', 'POST'])
def edit_course(course_id=None):
    course_id=int(course_id)
    course=database.get_course(course_id)
    if request.method == 'POST':
        print('clicked submit')
        name = request.form['Name']
        pet_type = request.form['Pet_Type']
        level = request.form['Level']
        start_date = request.form['Start_Date']
        start_time = request.form['Start_Time']
        course_duration = request.form['Course_Duration']
        course_length = request.form['Course_Length']
        trainer = request.form['Trainer']
        course_description= request.form['Description']
        database.update_course(course_id, name, pet_type, 
                level, start_date, start_time, course_duration, course_length, trainer, course_description)
        return redirect(url_for('course', course_id = course_id))
    else:  
        return render_template('add_course.html', course=course, course_id=course_id)

#add_attendee function allows the user to add attendee to the specific course,
# by taking the course_id and then transferring it. .form stores all the data that is
# then input on the attendee.html page. The button is stored in the course.html page.     
@app.route('/courses/<course_id>/attendees/add', methods =['GET', 'POST'])
def add_attendee(course_id):
    course_id=int(course_id)
    course=database.get_course(course_id)
    if request.method == 'POST':
        new_attendee = {}
        f_name =request.form['f_name']
        l_name =request.form['l_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        comment = request.form['comment']
        print(course)
        database.add_attendee(course_id, f_name, l_name, email, date_of_birth, comment)
        return redirect(url_for('course_list.html', course_id=course_id, course=course))
# Lastly, images are stored in static/images, styles in css/styles. courses.csv
# includes the data used for the app. 