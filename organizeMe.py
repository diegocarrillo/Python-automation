import os
from pathlib import Path
import re

pattern = '*'

SUBDIRECTORIES = {
    "DOCUMENTS": ['/*.pfd', '/*.rtf', '/*.txt', '*.doc', '*.docx'],
    "AUDIO": ['*.mp3', '*.m4a', '*.m4b'],
    "VIDEOS": ['*.mkv', '*.avi', '*.mp4'],
    "COMPRESSED": ['*.zip', '*.rar'],
    "SOFTWARE": ['*.exe', '*.msi'],
    "IMAGES": ['*.jpg', '*.jpeg', '*.png']
}

def picCategory(value):
    for category, suffixes in SUBDIRECTORIES.items( ):
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = picCategory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()