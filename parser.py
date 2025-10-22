"""
parser.py: functions to parse resumes and fetch profile information
"""

from typing import Dict, Any


def parse_resume(file_path: str) -> Dict[str, Any]:
    """
    Parse a resume/CV file and return structured information such as name, email, skills, education, experience.

    This function can use third-party libraries like Pyresparser or pdfplumber to extract text and parse details.
    For example, Pyresparser extracts data such as name, email, skills, education and more.
    """
    # TODO: implement resume parsing using appropriate libraries (e.g., pdfplumber, docx2txt, pyresparser)
    pass


def fetch_google_scholar_profile(profile_url: str) -> Dict[str, Any]:
    """
    Fetch author information and publication details from a Google Scholar profile.

    This function can use the 'scholarly' library to search author by Google Scholar ID or URL and retrieve
    citation counts and publication metadata.
    """
    # TODO: implement Google Scholar data retrieval using scholarly library
    pass


def fetch_orcid_profile(orcid_id: str) -> Dict[str, Any]:
    """
    Fetch researcher profile information from ORCID.

    This function can use the PyORCID (pyorcid) library to interact with the ORCID API and obtain
    publications and other research activities.
    """
    # TODO: implement ORCID data retrieval using pyorcid or ORCID API
    pass
