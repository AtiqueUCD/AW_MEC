from flask import Flask, request, Response
from PIL import Image, ImageFilter
from io import BytesIO
import time

app = Flask(__name__)

def apply_grayscale_and_edges(image):
    gray_image = image.convert('L')
    edge_image = gray_image.filter(ImageFilter.FIND_EDGES)
    return edge_image

@app.route('/thumbnail', methods=['POST'])
def thumbnail():
    start_time = time.time()
    
    file = request.files['file']
    image = Image.open(file.stream)
    
    processed_image = apply_grayscale_and_edges(image)

    img_io = BytesIO()
    processed_image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)

    processing_time = time.time() - start_time
    response = Response(img_io.getvalue(), mimetype='image/jpeg')
    response.headers['X-Processing-Time'] = f"{processing_time:.2f}s"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
