"""
generator.py

This module contains functions for generating a personal website from parsed resume/profile data.
The website is built from a template using Tailwind CSS for styling. This is part of Step 2
(Template-Based Website Generation) of the ScholarAIO MVP.

The function generate_website() takes structured data extracted from a CV/resume or profiles
(like Google Scholar or ORCID) and returns a complete HTML document. The default template is
defined inline and uses Tailwind CSS for basic styling. Users can optionally supply a different
template file path.

"""

from typing import Dict, Optional

def generate_website(data: Dict[str, any], template_path: Optional[str] = None, output_path: Optional[str] = None) -> str:
    """
    Generate a personal website HTML from structured data.

    Args:
        data (Dict[str, any]): Dictionary containing fields such as 'name', 'bio',
            'education', 'experience', 'publications', etc., produced by the parsing step.
        template_path (Optional[str]): Path to a custom HTML template. If None, a built-in
            template with Tailwind CSS is used.
        output_path (Optional[str]): If provided, the generated HTML will be saved to this file path.

    Returns:
        str: The generated HTML as a string.

    Example:
        parsed_data = {
            'name': 'Jane Doe',
            'bio': 'Research scientist in AI.',
            'education': [...],
            'experience': [...],
            'publications': [...]
        }
        html = generate_website(parsed_data)
    """
    # Define a simple default template with Tailwind CSS
    default_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Personal Website</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 text-gray-900">
    <div class="max-w-4xl mx-auto py-8 px-4">
        <h1 class="text-4xl font-bold mb-4">{name}</h1>
        <p class="mb-6">{bio}</p>

        <!-- Education Section -->
        {{education_section}}

        <!-- Experience Section -->
        {{experience_section}}

        <!-- Publications Section -->
        {{publications_section}}
    </div>
</body>
</html>"""

    # Load template from file if provided
    template_str = default_template
    if template_path:
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_str = f.read()
        except FileNotFoundError:
            # Fall back to default template if file not found
            pass

    # Build sections from data
    education_section = ""
    if data.get('education'):
        education_section += "<h2 class=\"text-2xl font-semibold mb-2\">Education</h2>\n<ul class=\"mb-4\">\n"
        for edu in data['education']:
            education_section += f"<li class=\"mb-1\">{edu}</li>\n"
        education_section += "</ul>\n"

    experience_section = ""
    if data.get('experience'):
        experience_section += "<h2 class=\"text-2xl font-semibold mb-2\">Experience</h2>\n<ul class=\"mb-4\">\n"
        for exp in data['experience']:
            experience_section += f"<li class=\"mb-1\">{exp}</li>\n"
        experience_section += "</ul>\n"

    publications_section = ""
    if data.get('publications'):
        publications_section += "<h2 class=\"text-2xl font-semibold mb-2\">Publications</h2>\n<ul class=\"mb-4\">\n"
        for pub in data['publications']:
            publications_section += f"<li class=\"mb-1\">{pub}</li>\n"
        publications_section += "</ul>\n"

    # Combine sections into template
    html_output = template_str.format(
        name=data.get('name', 'Unknown'),
        bio=data.get('bio', ''),
    ).replace('{{education_section}}', education_section)\
     .replace('{{experience_section}}', experience_section)\
     .replace('{{publications_section}}', publications_section)

    # Save to file if output_path provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

    return html_output
