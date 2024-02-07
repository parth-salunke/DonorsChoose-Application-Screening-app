from dataclasses import dataclass
from pathlib import Path


"""
entity - its return type of given function - datainvestigation

dataclass is decorator -
it applies on python class so it will work as entity
it wont be Python class it will be class var

"""

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path