import os
import json

# Get project root dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

# Ensure it doesn't look in site-packages
if "site-packages" in PROJECT_ROOT:
    PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "../../.."))

CONFIG_FILE = os.path.join(PROJECT_ROOT, "settings.json")
STRUCTURE_FILE = os.path.join(PROJECT_ROOT, "default_structure.json")

def load_config():
    """Loads course directory from settings.json. Defaults to current directory if missing."""
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ Warning: Config file not found at {CONFIG_FILE}. Using current directory.")
        return os.getcwd()

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        return config.get("course_directory", os.getcwd())

def load_structure():
    """Loads the default Udemy course structure from JSON."""
    if not os.path.exists(STRUCTURE_FILE):
        print(f"❌ Warning: Structure config file not found at {STRUCTURE_FILE}. Using defaults.")
        return {
            "directories": [
                "01-Introduction",
                "02-Getting-Started",
                "03-Building-the-Project",
                "04-Advanced-Topics",
                "05-Deployment",
                "06-Bonus-Materials",
                "07-Conclusion"
            ],
            "files": ["README.md", ".gitignore"]
        }

    with open(STRUCTURE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def create_project_structure(course_name):
    """Creates a structured Udemy course directory."""
    base_dir = load_config()
    structure = load_structure()

    project_path = os.path.join(base_dir, course_name)
    os.makedirs(project_path, exist_ok=True)

    for directory in structure["directories"]:
        os.makedirs(os.path.join(project_path, directory), exist_ok=True)

    for file in structure["files"]:
        file_path = os.path.join(project_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")

    print(f"✅ Course project structure created at: {project_path}")
