import os
from pathlib import Path
from datetime import datetime, timedelta

# Thresholds
LARGE_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
OLD_FILE_DAYS = 365

SCREENSHOT_KEYWORDS = ["screenshot", "screen_shot", "screen-shot"]
ARCHIVE_EXTENSIONS = [".zip", ".rar", ".7z", ".tar", ".gz"]


def analyze_files(file_objects):
    large_files = []
    old_files = []
    screenshots = []
    archive_files = []
    duplicates = {}

    current_time = datetime.now()

    for file in file_objects:

        # Large Files
        if file.size >= LARGE_FILE_SIZE:
            large_files.append(file)

        # Old Files
        if datetime.fromtimestamp(file.modified_time) < current_time - timedelta(days=OLD_FILE_DAYS):
            old_files.append(file)

        # Screenshots
        if any(word in file.name.lower() for word in SCREENSHOT_KEYWORDS):
            screenshots.append(file)

        # Archive Files
        if file.extension.lower() in ARCHIVE_EXTENSIONS:
            archive_files.append(file)

        # Duplicate Detection (name + size)
        key = (file.name.lower(), file.size)

        if key not in duplicates:
            duplicates[key] = []

        duplicates[key].append(file)

    duplicate_files = {
        k: v for k, v in duplicates.items()
        if len(v) > 1
    }

    return {
        "large_files": large_files,
        "old_files": old_files,
        "screenshots": screenshots,
        "archive_files": archive_files,
        "duplicates": duplicate_files,
    }


def find_empty_folders(folder_path):
    empty_folders = []

    for root, dirs, files in os.walk(folder_path):
        if not dirs and not files:
            empty_folders.append(root)

    return empty_folders
