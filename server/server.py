from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/api/home',methods = ['GET'])
def return_home():
    return jsonify({
        'message': 'hello lolz'
    })

@app.route('/api/get',methods=["POST"])
def take_val():
    data = request.json
    value = data.get('value')
    print(value)
    return jsonify({
        'reciveed' : value
    })


   

if __name__ == '__main__':
    app.run(debug = True,port=8080)
    