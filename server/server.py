from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/home',methods = ['GET'])
def return_home():
    return jsonify({
        'message': 'hello lolz'
    })
#sends in a post request and recieves whatever value is passed in by the frontend

@app.route('/api/get',methods=["POST"])
def take_val():
    data = request.json
    value = data.get('value')
    print(value)
    return jsonify({
        'reciveed' : value
    })
#todo: make two different tables, one for jobs and one for users
#todo: put this value {recieved as a list}in postgres database of user preferences

   

if __name__ == '__main__':
    app.run(debug = True,port=8080)
    