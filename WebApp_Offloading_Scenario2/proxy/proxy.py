from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)
server_url = "http://server:5000/thumbnail"

@app.route('/thumbnail', methods=['POST'])
def proxy_request():
    files = {'file': (request.files['file'].filename, request.files['file'].stream, request.files['file'].content_type)}
    response = requests.post(server_url, files=files)
    processing_time = response.headers.get('X-Processing-Time', 'unknown')

    return Response(response.content, response.status_code, mimetype=response.headers['Content-Type'], headers={"X-Processing-Time": processing_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
