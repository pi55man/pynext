from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chauhan@localhost/freelance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    password = db.Column(db.String(120),nullable=False)
    preferences = db.Column(db.JSON,nullable = True)

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/getdb',methods=['GET'])
def check_db():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({'message':"Database connected"})
    except OperationalError:
            return jsonify({'message':"database connection failed"})

@app.route('/api/home',methods = ['GET'])
def return_home():
    return jsonify({
        'message': 'hello arin'
    })
#sends in a post request and recieves whatever value is passed in by the frontend

@app.route('/api/get',methods=["POST"])
def take_prefs():
    data = request.json
    preferences = data.get('preferences',[])#extract the preferences in a list
    
    #TODO : store in postgres here, with user name, password and stuff
    
    print(preferences)
    return jsonify({"message": "recieved prefs"})

#TODO: make two different tables, one for jobs and one for users
#TODO: put this value {recieved as a list}in postgres database of user preferences
#TODO: process this value against the jobs database and return most relevant jobs

   

if __name__ == '__main__':
    app.run(debug = True,port=8080)
    