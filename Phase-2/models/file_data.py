from pathlib import Path
from datetime import datetime


class FileData:
    def __init__(self, file_path):
        self.path = Path(file_path)
        self.name = self.path.stem
        self.extension = self.path.suffix
        self.size = self.path.stat().st_size
        self.location = str(self.path.resolve())
        self.created = datetime.fromtimestamp(
            self.path.stat().st_ctime
        ).strftime("%Y-%m-%d %H:%M:%S")
        self.modified = datetime.fromtimestamp(
            self.path.stat().st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Extension: {self.extension}\n"
            f"Size: {self.size} bytes\n"
            f"Location: {self.location}\n"
            f"Created: {self.created}\n"
            f"Modified: {self.modified}\n"
        )
