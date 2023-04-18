import pymysql

#uncomment the following line when you start project 3.2:
from app import app


# Make sure you have data in your tables. You should have used auto increment for 
# primary keys, so all primary keys should start with 1

#you will need this helper function for all of your functions
#Use the uncommented version to test and turn in your code.  
#Comment out this version and then uncomment and use the second version below when you are importing 
#this file into your app.py in your I211_project for Project 3.2
# def get_connection():
#     return pymysql.connect(host="db.luddy.indiana.edu",
#                            user="i211f22_jschrum",
#                            password="my+sql=i211f22_jschrum",
#                            database="i211f22_jschrum",
#                            cursorclass=pymysql.cursors.DictCursor)

def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)

def get_courses():
    #Returns a list of dictionaries representing all of the courses data
    #add your code below, deleting the "pass"
    sql = "select * from course order by course_name"
    conn = get_connection()
    with conn: 
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

def get_course(course_id):
    #Takes a course_id, returns a single dictionary containing the data for a course with that id
    sql = "select * from course where course_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course_id))
            return cursor.fetchone()
def add_course(course_name, pet_type, course_level, start_date, start_time, course_duration, course_length, trainer, description):
    #Takes as input all of the data for a course. Inserts a new course into the course table
    sql = "INSERT INTO course (course_name, pet_type, course_level, start_date, start_time, course_duration, course_length, trainer, description)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course_name, pet_type, course_level, start_date, start_time, course_duration, course_length, trainer, description))
        conn.commit()

def update_course(c_id,Name, Pet_Type, Level, Start_Date, Start_Time, Course_Duration, Course_Length, Trainer, Description):
    #Takes a course_id and data for a course. Updates the course table with new data for the course with
    #course_id as it's primary key
    sql = "UPDATE course SET course_name=%s, pet_type=%s, course_level=%s, start_date=%s, start_time=%s, course_duration=%s, course_length=%s, trainer=%s, description=%s WHERE course_id= %s"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (Name, Pet_Type, Level, Start_Date, Start_Time, Course_Duration, Course_Length, Trainer, Description,c_id))
        conn.commit()
def add_attendee(course_id, f_name, l_name, phone_number, email, date_of_birth, comment):
    #Given a course_id and attendee info, adds a new attendee to the attendee table
    sql = "INSERT INTO attendee (course_id, f_name, l_name, phone_number, email, date_of_birth, comment) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (course_id, f_name, l_name, phone_number, email, date_of_birth, comment))
        conn.commit()

def edit_attendee(attendee_id, course_id, f_name, l_name, phone_number, email, date_of_birth):
    #Given an attendee__id and attendee info, updates the data for the attendee with the given attendee_id the attendee table
    sql = "UPDATE attendee SET f_name=%s, l_name=%s, phone_number=%s, email=%s, date_of_birth=%s WHERE attendee_id=%s AND course_id=%s"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (f_name, l_name, phone_number, email, date_of_birth, attendee_id, course_id))
            return cursor.fetchone()

def delete_attendee(attendee_id, course_id):
    #Takes an attendee_id and deletes the attendee with that attendee_id from the attendee table
    sql = "DELETE FROM attendee WHERE attendee_id=%s AND course_id=%s"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (attendee_id, course_id))
            return cursor.fetchone()

if __name__ == '__main__':
    #add more test code here to make sure your functions are working correctly
    try:
        print(f'All courses: {get_courses()}')
        #print(f'Course info for course_id 1: {get_course(1)}')
    
        #add_course("New Paws", "dog", "beginner", "2022-12-03", "09:00:00", 60, 6, "Lassie Shepherd", "For newbie dog owners!" )
        delete_attendee(2, 3)
        print(f'All courses: {get_courses()}')

        #add_attendee(1,"Tom", "Sawyer","812-905-1865","tsawyer@twain.com","1970-04-01")
    except Exception as e:
        print(e)