import os
from donorschoose import logger
import re
from pathlib import Path
import pandas as pd
import numpy as np
from tqdm import tqdm
from donorschoose.entity.config_entity import DataCleanConfig
from donorschoose.config.configuration import ConfigurationManager
from donorschoose.utils.common import read_csv, read_txt_file
from sklearn.preprocessing import StandardScaler


class DataCleaning:
    def __init__(self, config: DataCleanConfig):
        self.config = config
        self.train_df = None
        self.resource_df = None
        self.stopwords= None

    def read_files(self):
        '''
        Fetches data from the specified URLs and returns DataFrames.
        '''
        try: 
            root_dir = self.config.root_dir
            os.makedirs(root_dir, exist_ok=True)
            train_path = Path(self.config.local_data_trainfile)
            
            resource_path = Path(self.config.local_data_resourcefile)
            stopword_txt_path = Path(self.config.local_data_stopwordsfile)
            self.train_df = read_csv(train_path)
            self.resource_df = read_csv(resource_path)
            self.stopwords = read_txt_file(stopword_txt_path)
            
        except Exception as e:
            raise e
    
    def clean_text_column(self, column:str ):
        """
        this function will remove Spaces and special char from text column
        
        if we have any Nan value then it will fill nan value with 
        whatever have max count category
        """

        self.train_df[column] =self.train_df[column].str.replace(' ','_')
        self.train_df[column] =self.train_df[column].str.replace(',','_')
        self.train_df[column] =self.train_df[column].str.replace('.','')
        self.train_df[column] =self.train_df[column].str.replace('-','_')
        self.train_df[column] =self.train_df[column].str.replace('&','_')
        self.train_df[column] =self.train_df[column].str.replace(' The ','')
        self.train_df[column] =self.train_df[column].str.lower()
        self.train_df[column] =self.train_df[column].str.replace('___','_')
        self.train_df[column] =self.train_df[column].str.replace('__','_')
        
        max_count_id = self.train_df[column].value_counts().idxmax()
        self.train_df[column]=self.train_df[column].fillna(max_count_id)
        
        logger.info(f"preprocessed column :{column} , unique categories Count : {len(self.train_df[column].value_counts())}")

    def add_two_column(self , column1: str , column2: str):
        try:
            if column1 not in self.train_df.columns:
                self.train_df[column1] = self.train_df[column2].astype(str)
            else:
                self.train_df[column1] += self.train_df[column2].astype(str)

        except Exception as e:
            raise e
        
    def decontracted(self ,phrase: str) -> str:
            # specific
        phrase = re.sub(r"won't", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        
        return phrase

    def preprocess_text(self ,column:str)-> list:
        text_list = self.train_df[column].values
        preprocessed_text = []
        try:
            for sentance in tqdm(text_list):
                sent = self.decontracted(sentance)
                sent = sent.replace('\\r', ' ')
                sent = sent.replace('\\n', ' ')
                sent = sent.replace('\\"', ' ')
                sent = re.sub('[^A-Za-z0-9]+', ' ', sent)
                sent = ' '.join(e for e in sent.split() if e.lower() not in self.stopwords)
                preprocessed_text.append(sent.lower().strip())
            logger.info(f"preprocessed column :{column}")
            self.train_df[column]=preprocessed_text
        
        except Exception as e:
            raise e

    def merge_csv(self):
        """
        joining two dataframes in python
        """
        try:
            self.resource_df = self.resource_df.groupby('id').agg({'price':'sum', 'quantity':'sum'}).reset_index()
            self.train_df =pd.merge(self.train_df, self.resource_df, on='id', how='left')
            logger.info(f"aggrigated resourde df and merged both df")
        except Exception as e:
            raise e

    def drop_colums(self , column_list : list):
        self.train_df = self.train_df.drop(column_list, axis=1)
        logger.info(f"dropped columns:{column_list}")
        
    def rename_column(self ,columnNanme:str , newName : str):
        self.train_df = self.train_df.rename(columns={
            columnNanme: newName,
            })
        logger.info(f"renamed column:{columnNanme} to {newName}")
        
    
    