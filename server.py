"""
Server module for ScholarAIO MVP.
Provides a minimal Flask web server to accept resume uploads or profile links,
parse the input using parser functions, generate HTML using the generator module, and return the result.
"""

from flask import Flask, request
from parser import parse_resume, fetch_google_scholar_profile, fetch_orcid_profile
from generator import generate_website
import os
import tempfile

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate():
    """Endpoint to handle resume upload or profile link submission and return generated website HTML."""
    data = {}
    # Handle file upload from form field named 'file'
    if 'file' in request.files:
        uploaded_file = request.files['file']
        if uploaded_file.filename:
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, uploaded_file.filename)
            uploaded_file.save(file_path)
            # Parse the resume using parser module
            parsed_data = parse_resume(file_path)
            if parsed_data:
                data.update(parsed_data)
    # Handle link submission from form field named 'link'
    link = request.form.get('link')
    if link:
        if 'scholar.google' in link:
            scholar_data = fetch_google_scholar_profile(link)
            if scholar_data:
                data.update(scholar_data)
        elif 'orcid' in link:
            orcid_data = fetch_orcid_profile(link)
            if orcid_data:
                data.update(orcid_data)
    # Generate website HTML using the generator module
    html_content = generate_website(data)
    return html_content, 200, {'Content-Type': 'text/html'}


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
