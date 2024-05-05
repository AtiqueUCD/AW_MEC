from flask import Flask, request, render_template, redirect, url_for, Response
import requests
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', original_image=None, processed_image=None, processing_time=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    if file:
        original_data = file.read()
        original_image = base64.b64encode(original_data).decode('utf-8')
        
        file.seek(0)
        files = {'file': (file.filename, file.stream, file.content_type)}
        response = requests.post('http://proxy:5000/thumbnail', files=files)
        processing_time = response.headers.get('X-Processing-Time', 'N/A')
        
        processed_image = base64.b64encode(response.content).decode('utf-8')
        
        return render_template('index.html', original_image=original_image, processed_image=processed_image, processing_time=processing_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
