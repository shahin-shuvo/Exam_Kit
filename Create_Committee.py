import gc

from flask import Flask, render_template, request, flash, session, url_for, redirect, jsonify, make_response, json


class Committee_Class:
    def __init__(self, mysql):
        self.mysql = mysql

    def pass_data(self):
        error = ''
        data1 = []
        i = 0
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SyllabusID FROM   syllabus ORDER BY syllabus.SyllabusID DESC")
            SYL = cursor.fetchall()
            cursor.execute(
                "SELECT Name FROM   Teacher WHERE Designation= 'Professor'")
            Name1 = cursor.fetchall()
            cursor.execute(
                "SELECT Name FROM   Teacher WHERE Designation= 'Associate Professor'")
            Name2 = cursor.fetchall()
            cursor.execute(
                "SELECT Name FROM   Teacher WHERE Designation= 'Assistant Professor'")
            Name3 = cursor.fetchall()
            cursor.execute(
                "SELECT Name FROM   Teacher WHERE Designation= 'Lecturer'")
            Name4 = cursor.fetchall()

            return render_template("index_1.html", SYL=SYL, Name1=Name1, Name2=Name2, Name3=Name3, Name4=Name4)


        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"

    def create(self):
        try:
            query = request.args['query']
            query = json.loads(query)

            conn = self.mysql.connect()
            x = conn.cursor()

            data = (query[0], query[1], query[2], query[3], query[4], query[5], query[6], query[7], query[8])
            x.execute("INSERT INTO Committee (Name,syl_id,sdate,endate,year,chairman,gm1,gm2,exm) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",data)

            conn.commit()
            conn.close()
            return "OK"
        except Exception as e:
            return (str(e))
