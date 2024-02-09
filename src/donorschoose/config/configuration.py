from donorschoose.constants import *
import os
from donorschoose.utils.common import read_yaml, create_directories
from donorschoose.entity.config_entity import (DataIngestionConfig)
from donorschoose.entity.config_entity import (DataCleanConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        # params_filepath = PARAMS_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        # self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        """
        it will take config for data ingestion from config.yaml and
        store it in entity object DataIngestionConfig which we create it in entity 
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_data_clean_config(self) -> DataCleanConfig:
        config = self.config.data_cleaning
        create_directories([config.root_dir])

        data_clean_config = DataCleanConfig(
            root_dir=config.root_dir,
            local_data_trainfile=config.local_data_trainfile,
            local_data_resourcefile=config.local_data_resourcefile,
            local_data_stopwordsfile =config.local_data_stopwordsfile,
            save_clean_datafile = config.save_clean_datafile
        )
        return data_clean_config
    