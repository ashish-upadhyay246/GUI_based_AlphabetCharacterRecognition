from flask import Flask, render_template, request, jsonify
import cv2
from PIL import ImageGrab
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    # Your drawing logic here
    # Access data from the frontend using request.json
    data = request.json
    # Process data and perform drawing

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
