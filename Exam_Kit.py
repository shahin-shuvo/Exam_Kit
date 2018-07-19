from flask import Flask,render_template, request, session
from flaskext.mysql import MySQL
from Login import *
from Create_Committee import *
from Existing_Committee import *
from Teacher import *

app = Flask(__name__)
mysql = MySQL()
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '$huvo919671'
# app.config['MYSQL_DATABASE_DB'] = "Du_Booking_Data"
#app.config['MYSQL_DATABASE_PASSWORD'] = DB_PASS
app.config['MYSQL_DATABASE_DB'] = "Exam_Kit"
mysql.init_app(app)

username = "Guest$"
user_type = "#$"
logged_in = False


@app.route('/')
def start():
    try:
      if session['logged_in'] == True and session['user_type']== "admin":
        #return render_template('index_1.html')
        return Committee_Class(mysql).pass_data()
      elif session['logged_in'] == True and session['user_type']== "teacher":
          return Teacher_Class(mysql).load_main()

    except Exception as e:
        return render_template('main_page.html')


@app.route('/index',methods=["GET","POST"])
def index():
    return Committee_Class(mysql).pass_data()

@app.route('/create',methods=["GET","POST"])
def create():
    return Committee_Class(mysql).create()

@app.route('/existing_committee',methods=["GET","POST"])
def existing_committee():
    return Existing_Committee_Class(mysql).show()

@app.route('/modal_query',methods=["GET","POST"])
def modal_query():
    return Teacher_Class(mysql).modal_data()


@app.route('/course_data',methods=["GET","POST"])
def course_data():
    return Teacher_Class(mysql).course_data()

@app.route('/addNewCourse',methods=["GET","POST"])
def addNewCourse():
    return Teacher_Class(mysql).addNewCourse()

@app.route('/login_helper', methods=["GET", "POST"])
def login_helper():
    return Login_Class(mysql).login_helper()


@app.route('/teacher_main',methods=["GET","POST"])
def teacher_main():
    return Teacher_Class(mysql).load_main()

@app.route("/logout")
def logout():
    session.clear()
    gc.collect()
    return render_template("main_page.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
