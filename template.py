import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"srs/{project_name}/__init__.py",
    f"srs/{project_name}/components/__init__.py",
    f"srs/{project_name}/utils/__init__.py",
    f"srs/{project_name}/utils/common.py",
    f"srs/{project_name}/logging/__init__.py",
    f"srs/{project_name}/config/__init__.py",
    f"srs/{project_name}/utils/configuration.py",
    f"srs/{project_name}/pipeline/__init__.py",
    f"srs/{project_name}/entity/__init__.py",
    f"srs/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"{filename} already exists")
