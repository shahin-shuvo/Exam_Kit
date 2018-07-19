import gc
from json import dumps

import math
from flask import Flask, render_template, request, flash, session, url_for, redirect, jsonify, make_response, json


class Teacher_Class:
    def __init__(self, mysql):
        self.mysql = mysql

    def load_main(self):
        try:
           name =  session['username']

           conn = self.mysql.connect()
           cursor = conn.cursor()
           cursor.execute("SELECT Name  FROM Teacher WHERE Username = (%s)",(name))
           teacher_name = cursor.fetchall()

           cursor.execute("SELECT * FROM Committee WHERE chairman = (%s) OR gm1 = (%s) OR gm1 = (%s) OR exm = (%s)",
                            (teacher_name,teacher_name,teacher_name,teacher_name))
           data = cursor.fetchall()
           count = len(data)
           row_count= math.floor(count/3)+1

           return render_template("teacher_main.html",data = data,count =  count,row_count=int(row_count))



        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"

    def modal_data(self):
        try:
            committee_ind = request.args['query']
            conn = self.mysql.connect()
            cursor = conn.cursor()
            name = session['username']
            cursor.execute("SELECT Name  FROM Teacher WHERE Username = (%s)", (name))
            teacher_name = cursor.fetchall()

            cursor.execute("SELECT * FROM Committee WHERE chairman = (%s) OR gm1 = (%s) OR gm1 = (%s) OR exm = (%s)",
                           (teacher_name, teacher_name, teacher_name, teacher_name))
            data = cursor.fetchall()

            return make_response(dumps(data))
        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"

    def course_data(self):
        try:
            committee_ind = request.args['query']
            conn = self.mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM courses")
            course_data = cursor.fetchall()
            return make_response(dumps(course_data))
        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"

    def addNewCourse(self):
        try:
            query = request.args['query']
            cData = json.loads(query)

            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO courses (CourseID,Title,Year,Semester,Credit) VALUES (%s, %s, %s,  %s, %s)",
                (cData[0],cData[1],cData[2],cData[3],cData[4]))
            conn.commit()
            conn.close()
            return "0"
        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"