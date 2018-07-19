import gc
from json import dumps

from flask import Flask, render_template, request, flash, session, url_for, redirect, jsonify, make_response, json


class Existing_Committee_Class:
    def __init__(self, mysql):
        self.mysql = mysql

    def show(self):
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT  * FROM   Committee")

            name = cursor.fetchall()
            limit = len(name)
            return render_template("existing_committee.html", limit=limit, committee_data=name)



        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"


    def modal_data(self):
        try:

            committee_name = request.args['query']
            conn = self.mysql.connect()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT  * FROM   Committee WHERE Name= %s",(committee_name,))
            committee_data = cursor.fetchall()
            print(committee_data)
            return make_response(dumps(committee_data))
        except Exception as e:
            # flash(e)
            error = "Invalid credentials, try again."
            return "Error"
