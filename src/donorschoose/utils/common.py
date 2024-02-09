import os
from box.exceptions import BoxValueError
import yaml
from donorschoose import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import pandas as pd
import csv


"""
ConfigBox - its uses dict as config param
example  - tempDict =   {
                            "alpha" : "0.1" , 
                            "C"    : "1"
                        }

if we want to fetch values in python dict we need to do tempDict["alpha"]
by wrapping dict in configbox we can do tempDict.alpha

@ensure_annotations -
we use ensure annottation to ensure that we are passing correct datatype 

"""


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def read_csv(path_to_csv: Path) -> pd.core.frame.DataFrame:
    """reads csv file and returns 

    Args:
        path_to_csv (str): path like input

    Raises:
        e: empty file

    Returns:
        pd.core.frame.DataFrame
    """
    try:
        # Specify the encoding parameter
        with open(path_to_csv, encoding='utf-8') as csv_file:
            dataframe = pd.read_csv(csv_file)
            logger.info(f"csv file: {path_to_csv}, df Shape:{dataframe.shape} loaded successfully")
            return dataframe
    except Exception as e:
        raise e

@ensure_annotations
def read_txt_file(path_to_txt: Path) -> list:
    """reads txt file and returns 

    Args:
        path_to_txt (str): path like input

    Raises:
        e: empty file

    Returns:
       list
    """
    try:
        with open(path_to_txt, "r", encoding='utf-8') as f:
            stopwords_string = f.read()

        stopwords = [word.strip() for word in stopwords_string.split('\n') if word.strip()]

        logger.info(f"stopword file: {path_to_txt}, Number of words :{len(stopwords)} loaded successfully")
        return  stopwords
    except Exception as e:
        raise e

@ensure_annotations
def save_csv(data_frame,file_path ):
    """get size in KB

    Args:
        path (Path): path of the file

    filtered_resource_data.to_csv('fi ltered_resource_data1000.csv', index=False) 
    """
    file_path = Path(file_path)
    data_frame.to_csv(file_path, index=False) 
    logger.info(f"save dataframe in {file_path}")
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
                 
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
