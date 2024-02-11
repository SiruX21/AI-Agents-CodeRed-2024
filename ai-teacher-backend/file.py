from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS  # Import the CORS library
app = Flask(__name__)
CORS(app) 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file and file.filename.endswith('.txt'):
        filename = secure_filename(file.filename)
        file.save(os.path.join('transcriptions', filename))
        return 'File saved successfully', 200

    return 'Invalid file type. Only .txt files are allowed', 400

if __name__ == '__main__':
    if not os.path.exists('transcriptions'):
        os.makedirs('transcriptions')
    app.run(debug=True, port=6050)