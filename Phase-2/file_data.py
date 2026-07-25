from dataclasses import dataclass

@dataclass
class FileData:
    name: str
    extension: str
    size: int
    path: str
    created_time: float
    modified_time: float
