import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

CONFIG_FILE = os.path.join(PROJECT_ROOT, "settings.json")
STRUCTURE_FILE = os.path.join(PROJECT_ROOT, "default_structure.json")

def load_config():
    """Loads course directory from settings.json or defaults to ~/Documents/UdemyCourses."""
    default_path = os.path.expanduser("~/Documents/UdemyCourses")

    if not os.path.exists(CONFIG_FILE):
        return default_path

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        return config.get("course_directory", default_path)

def load_structure():
    """Loads the default Udemy course structure from JSON."""
    if not os.path.exists(STRUCTURE_FILE):
        return {
            "sections": {
                "Section01": ["Lecture01"]
            }
        }

    with open(STRUCTURE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def create_project_structure(course_name):
    """Creates a structured Udemy course directory dynamically from `default_structure.json`."""
    base_dir = load_config()  # Load directory from settings.json
    course_path = os.path.join(base_dir, course_name)
    os.makedirs(course_path, exist_ok=True)

    structure = load_structure()
    for section, lectures in structure["sections"].items():
        section_path = os.path.join(course_path, section)
        os.makedirs(section_path, exist_ok=True)

        for lecture in lectures:
            lecture_path = os.path.join(section_path, lecture)
            os.makedirs(lecture_path, exist_ok=True)

    return os.path.abspath(course_path)  # Ensure absolute path is returned
