from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/prompt', methods=['GET'])
def receive_data():
    parameter_value = request.args.get('prompt')
    print('Received parameter value:', parameter_value)
    return jsonify({'message': 'Data received successfully'}), 200