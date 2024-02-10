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
    
@dataclass(frozen=True)
class DataCleanConfig:
    root_dir: Path
    local_data_trainfile: Path
    local_data_resourcefile: Path
    local_data_stopwordsfile: Path
    save_clean_datafile: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    local_data_cleanfile: Path
    save_transformed_datafile: Path