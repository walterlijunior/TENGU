from flask import Flask, request, jsonify, send_file
from services.ocr_service import extract_text_from_image
from services.translation import translate_text
from services.image_overlay import overlay_translated_text
import os

app = Flask(__name__)

UPLOAD_FOLDER = '../storage/uploads'
PROCESSED_FOLDER = '../storage/processed'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = extract_text_from_image(filepath)
    translated_text = translate_text(text)

    processed_path = os.path.join(app.config['PROCESSED_FOLDER'], file.filename)
    overlay_translated_text(filepath, translated_text, processed_path)

    return send_file(processed_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
