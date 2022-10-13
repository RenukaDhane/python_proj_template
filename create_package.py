import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s:%(levelname)s]:%(message)s"
)

while True:
    package_name = input("Enter the name of the package: ")
    if package_name != '':
        break

logging.info(f"Creating package by name: {package_name}")

# list of files
list_of_files = [
  
    f"src/{package_name}/__init__.py",

]

for filepath in list_of_files:
    filedir, filename = os.path.split(Path(filepath))
    # if directory name is not empty then create a directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(
            f"Creating a directory at: {filedir} for file: {filename}")
    # if the file does not exist or size of file is zero i.e empty file then create a new file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file:{filename} at path:{filepath}")
    else:
        logging.info(f"file is already present at:{filepath}")
