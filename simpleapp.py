from flask import Flask, jsonify, request
import json
app = Flask(__name__)

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y
@app.route('/')
def say():
    return "hello we are functional right now"

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = add_numbers(data['x'], data['y'])
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = subtract_numbers(data['x'], data['y'])
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=5000)
