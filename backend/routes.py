from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from services.ocr_service import extract_text
from services.text_analysis_service import analyze_text
from utils.azure_storage import upload_to_azure

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = f"/tmp/{filename}"
        file.save(file_path)

        # Upload to Azure
        upload_url = upload_to_azure(file_path, filename)

        # Extract text using OCR
        text = extract_text(file_path)

        # Analyze text
        analysis = analyze_text(text)

        return jsonify({
            'filename': filename,
            'upload_url': upload_url,
            'text': text,
            'analysis': analysis
        }), 200