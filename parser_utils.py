"""
parser_utils.py
Functions to parse resumes and generate personal websites.
"""

from typing import Dict, Any, Optional
import re
import os


def parse_resume(file_path: str) -> Dict[str, Any]:
    """
    Parse a resume file (PDF, DOCX, or plain text) and extract name, email, and resume text.
    """
    text = ""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            try:
                import PyPDF2  # type: ignore
                with open(file_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted:
                            text += extracted + "\n"
            except Exception:
                pass
        elif ext == ".docx":
            try:
                import docx  # type: ignore
                doc = docx.Document(file_path)
                text = "\n".join(p.text for p in doc.paragraphs)
            except Exception:
                pass
        if not text:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
    except Exception:
        text = ""

    # Extract name and email
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    name = lines[0] if lines else ""
    match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    email = match.group(0) if match else ""

    return {"name": name, "email": email, "resume_text": text[:1000]}


def generate_website(data: Dict[str, Any], output_path: Optional[str] = None) -> str:
    """
    Generate a simple HTML personal website using Tailwind CSS from structured data.
    """
    name = data.get("name", "Anonymous")
    email = data.get("email", "")
    resume_text = data.get("resume_text", "")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Personal Website</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans">
    <div class="max-w-3xl mx-auto p-6">
        <header class="text-center mb-8">
            <h1 class="text-4xl font-bold">{name}</h1>
            <p class="text-gray-600">{email}</p>
        </header>
        <section class="mb-8">
            <h2 class="text-2xl font-semibold mb-2">About Me</h2>
            <p class="text-gray-700 whitespace-pre-wrap">{resume_text}</p>
        </section>
    </div>
</body>
</html>
"""

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
    return html
