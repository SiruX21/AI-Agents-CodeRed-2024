from dotenv import load_dotenv
from time import sleep
from flask import Flask, request
import logging, verboselogs, record, glob

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return {
        'msg': 'working'
    }

@app.route('/transcribe', methods = ['POST'])
def transcibe():
    if 'audio' not in request.files:
        return {
            'msg': 'No file found'
        }
    
    audio = request.files['audio'].read()
    transcription = record.transcribe(audio)

    filename = f'transcription_{len(glob.glob("*.txt")) + 1}'
    with open(filename, 'w') as f:
        f.write(transcription)

    return {
        'msg': transcription
    }
    
app.run("0.0.0.0", debug = True)