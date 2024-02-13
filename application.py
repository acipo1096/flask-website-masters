import os
from flask import Flask
from flask import render_template, request, flash
from models import db, Contact
from dotenv import load_dotenv
import smtplib

load_dotenv()

postgres = os.getenv('POSTGRES')
sqlalchemy_database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
secret_key = os.getenv('SECRET_KEY')
login = os.getenv('LOGIN')

def create_app():
  app = Flask(__name__)
  db.init_app(app)
  return app

app = create_app()
app.app_context().push()
app.config['TEMPLATES_AUTO_RELOAD'] = True
application = app

POSTGRES = postgres;
SQLALCHEMY_DATABASE_URI = sqlalchemy_database_uri
SECRET_KEY = secret_key

if __name__ == '__main__':
  db.create_all()
  app.run()

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = secret_key

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/technology/")
def technology():
  return render_template("technology.html")

@app.route("/music/")
def music():
  return render_template("music.html")


@app.route("/contact/")
def contact():
  return render_template("contact.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
  name = request.form["name"]
  email = request.form["email"]
  message = request.form["message"]
  entry = Contact(name=name, email=email, message=message)
  db.session.add(entry)
  db.session.commit()

  notification = 'You have received a new website form submission. Please log in to view.'
 
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(login, "")
  server.sendmail(login,login, notification)
  return render_template("contact.html")


# https://code.visualstudio.com/docs/python/tutorial-flask

# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask

# https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2

# https://www.reddit.com/r/learnpython/comments/bxumgw/typeerror_init_takes_1_positional_argument_but_6/