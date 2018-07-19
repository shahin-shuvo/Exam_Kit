
import gc

from flask import Flask, render_template, request, flash, session, url_for, redirect, jsonify, make_response, json


class Login_Class:
    def __init__(self, mysql):
        self.mysql = mysql

    def login_helper(self):
        error = ''
        try:
            query = request.args['query']
            query = json.loads(query)
            conn = self.mysql.connect()
            c = conn.cursor()
            if query[2] == "ADMIN":
                data = c.execute("SELECT * FROM Admin WHERE username = (%s) AND password = (%s)",
                                 (query[0], query[1]))
                if int(data) > 0:
                    session['logged_in'] = True
                    session['username'] = query[0]
                    session['user_type']="admin"
                    gc.collect()
                    return "OK_Admin"
            elif query[2] == "TEACHER":
                data = c.execute("SELECT * FROM Teacher WHERE Username = (%s) AND Password = (%s)",
                                 (query[0], query[1]))
                if int(data) > 0:
                    session['logged_in'] = True
                    session['username'] = query[0]
                    session['user_type'] = "teacher"
                    gc.collect()
                    return "OK_teacher"

            return "error"


        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"

