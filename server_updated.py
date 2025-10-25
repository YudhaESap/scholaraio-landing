"""
Updated Flask server that uses parser_utils for parsing resumes and generating personal websites.
"""

from flask import Flask, request
from parser_utils import parse_resume, generate_website
import os
import tempfile

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    """Endpoint to handle resume upload or profile link submission and return generated website HTML."""
    data = {}
    if 'file' in request.files:
        uploaded_file = request.files['file']
        if uploaded_file.filename:
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, uploaded_file.filename)
            uploaded_file.save(file_path)
            parsed = parse_resume(file_path)
            if parsed:
                data.update(parsed)
    link = request.form.get('link', '')
    if not data:
        return "No valid data provided.", 400
    html = generate_website(data)
    return html

if __name__ == '__main__':
    app.run(debug=True)
