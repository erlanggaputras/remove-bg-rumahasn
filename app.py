from flask import Flask, request, jsonify
from PIL import Image
from rembg import remove
import io
import base64
import numpy as np

app = Flask(__name__)

def base64_to_image_bytes(base64_str):
    return base64.b64decode(base64_str)

def image_bytes_to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    try:
        data = request.get_json()
        image_b64 = data['image_base64']

        # Ubah base64 ke bytes
        image_bytes = base64_to_image_bytes(image_b64)

        # Hapus background → hasilnya juga dalam bentuk bytes
        output_bytes = remove(image_bytes)

        # Ubah output ke base64 kembali
        output_b64 = image_bytes_to_base64(output_bytes)

        return jsonify({'image_base64': output_b64})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)